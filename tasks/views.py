from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse


def create_session_list(request):
    if 'tasks' not in request.session:
        request.session['tasks'] = []


class NewTask(forms.Form):
    task = forms.CharField(label='Task')


def index(request):
    create_session_list(request)

    return render(request, 'tasks/index.html', {
        'tasks': request.session['tasks']
    })


def add(request):
    create_session_list(request)

    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))

    return render(request, 'tasks/add.html', {
        'form': NewTask()
    })