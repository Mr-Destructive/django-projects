from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'djnotes'

urlpatterns = [
    path("", TemplateView.as_view(template_name="djnotes.html"), name="home"),

    path("note/", views.NotesListView.as_view(), name="note"),
    path("note/<int:pk>", views.NoteDetailView.as_view(), name="note_view"),
    path("note/create/", views.NoteCreateView.as_view(), name="create_note"),
    path("note/edit/<int:pk>", views.NoteUpdateView.as_view(), name="update_note"),
    path("note/delete/<int:pk>", views.NoteDeleteView.as_view(), name="delete_note"),

    path("books/", views.NotebookListView.as_view(), name="notebook"),
    path("books/<int:pk>", views.NotebookDetailView.as_view(), name="notebook_view"),
    path("books/create/", views.NotebookCreateView.as_view(), name="create_notebook"),
    path("books/edit/<int:pk>", views.NotebookUpdateView.as_view(), name="update_book"),
    path("books/delete/<int:pk>", views.NotebookDeleteView.as_view(), name="delete_book"),
    path("books/addnote/<int:pk>", views.AddNote.as_view(), name="add_note"),
    path(
        "books/addnote-existing/<int:pk>",
        views.AddExistingNote.as_view(),
        name="add_existing_note",
    ),
]
