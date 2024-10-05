from django.shortcuts import render

from .models import Note
from .forms import NoteForm


def get_init_context():
    all_notes = Note.objects.all()
    return {'notes': all_notes}


def index(request):
    context = get_init_context()

    return render(request, 'notes_app/index.html', context)


def get_note(request, pk):
    context = get_init_context()
    note = Note.objects.get(pk=pk)
    context['note'] = note

    return render(request, 'notes_app/note.html', context)


def create_note(request):
    context = get_init_context()

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(**form.cleaned_data)
            return index(request)
    else:
        form = NoteForm()

    context['form'] = form

    return render(request, 'notes_app/crt_nt.html', context)


def update_note(request, pk):
    context = get_init_context()
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = NoteForm(instance=note)

    context['form'] = form

    return render(request, 'notes_app/update_note.html', context)
