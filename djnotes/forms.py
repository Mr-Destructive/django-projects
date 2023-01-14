from django import forms
from .models import Note, Notebook


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ("created", "updated", "author")
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Name",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 900px;",
                    "placeholder": "Content",
                }
            ),
        }


class NotebookForm(forms.ModelForm):
    class Meta:
        model = Notebook
        exclude = (
            "created",
            "updated",
            "author",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Notebook Name",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Description",
                }
            ),
            "notes": forms.CheckboxSelectMultiple(),
        }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = (
            "created",
            "updated",
            "author",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 300px;",
                    "placeholder": "Note Name",
                }
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "max-width: 900px;",
                    "placeholder": "Content",
                }
            ),
        }


class AddExistingNoteForm(forms.ModelForm):
    class Meta:
        model = Notebook
        fields = [
            "notes",
        ]
        widgets = {
            "notes": forms.CheckboxSelectMultiple(),
        }
