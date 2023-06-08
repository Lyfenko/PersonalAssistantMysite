from django.shortcuts import render, redirect
from .forms import ContactForm, NoteForm
from .models import Contact, Note


def home(request):
    return render(request, 'home.html')


def contact_list(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts, 'query': query})


def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'add_contact.html', {'form': form})


def edit_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'edit_contact.html', {'form': form, 'contact': contact})


def delete_contact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()
    return redirect('contact_list')


def note_list(request):
    query = request.GET.get('q')
    if query:
        notes = Note.objects.filter(text__icontains=query)
    else:
        notes = Note.objects.all()
    return render(request, 'note_list.html', {'notes': notes, 'query': query})


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})


def edit_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'edit_note.html', {'form': form, 'note': note})


def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect('note_list')
