from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import NoteForm, NotebookForm, AddNoteForm, AddExistingNoteForm
from .models import Note, Notebook


class NoteView(View):
    model = Note
    template_name = "note/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["notes"] = Note.objects.filter(author=self.request.user).all()
        return context


class NoteSecureView(LoginRequiredMixin):

    model = Note

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        note = self.object
        if not (note.author == user or user.is_superuser):
            raise PermissionDenied
        return handler


class NotesListView(LoginRequiredMixin, NoteView, ListView):
    """View to list all notes."""

    template_name = "note/note_list.html"


class NoteDetailView(NoteSecureView, DetailView):
    """View to list the details from one note."""

    template_name = "note/note_detail.html"


class NoteCreateView(LoginRequiredMixin, NoteView, CreateView):
    """View to create a new Note"""

    form_class = NoteForm
    template_name = "note/add_note.html"
    success_url = "/dj-notes/note/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteCreateView, self).form_valid(form)


class NoteUpdateView(NoteSecureView, UpdateView):
    """View to update a Note"""

    form_class = NoteForm
    template_name = "note/edit_note.html"
    success_url = "/dj-notes/note"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NoteUpdateView, self).form_valid(form)


class NoteDeleteView(NoteSecureView, DeleteView):
    """View to delete a Note"""

    template_name = "note/delete_note.html"
    success_url = "/dj-notes/note"




class NotebookView(View):
    model = Notebook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = Notebook.objects.filter(author=self.request.user).all()
        return context


class NotebookSecureView(LoginRequiredMixin):

    model = Notebook

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        notebook = self.object
        if not (notebook.author == user or user.is_superuser):
            raise PermissionDenied
        return handler


class NotebookListView(LoginRequiredMixin, NotebookView, ListView):
    """View to list all notes."""

    template_name = "book/book_list.html"


class NotebookDetailView(NotebookSecureView, DetailView):
    """View to list the details from one note."""

    template_name = "book/book_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = Notebook.objects.get(id=self.kwargs["pk"])
        return context


class NotebookCreateView(NotebookView, CreateView):
    """View to create Notebook"""

    form_class = NotebookForm
    template_name = "book/create_notebook.html"
    success_url = "/dj-notes/books"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        user = self.request.user
        form.fields["notes"].queryset = Note.objects.filter(author=user)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NotebookCreateView, self).form_valid(form)


class NotebookUpdateView(NotebookSecureView, UpdateView):
    """View to update a Notebook"""

    form_class = NotebookForm
    template_name = "book/edit_book.html"
    success_url = "/dj-notes/books"


class NotebookDeleteView(NotebookSecureView, DeleteView):
    """View to delete a Notebook"""

    template_name = "book/delete_book.html"
    success_url = "dj-notes/books"


class AddNote(NotebookView, CreateView):
    """Create a Note in a Book"""

    form_class = AddNoteForm
    template_name = "book/create_note.html"
    success_url = "/dj-notes/books"

    def form_valid(self, form, **kwargs):
        form.instance.author = self.request.user
        response = super(AddNote, self).form_valid(form)
        book = Notebook.objects.get(id=self.kwargs["pk"])
        new_note = Note.objects.get(id=self.object.id)
        new_note.save()
        book.notes.add(new_note)
        book.save()
        return response


class AddExistingNote(NotebookSecureView, UpdateView):
    """Add an existing Note in a Book"""

    form_class = AddExistingNoteForm
    template_name = "book/add_existing_note.html"
    success_url = "/dj-notes/books"

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        user = self.request.user
        form.fields["notes"].queryset = Note.objects.filter(author=user)
        return form
