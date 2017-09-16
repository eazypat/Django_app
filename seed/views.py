from django.http import Http404
import datetime
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponseRedirect
from jinja2 import FileSystemLoader, Environment
from django.template.context_processors import csrf
from entry.HumanForm import HumanForm
from entry.models import Human

from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.shortcuts import render


def render_form(request, filename, context={}):
    return render(request, filename, Context(context))


def hello(request):
    return render_form(request, 'home.html', {'text': 'hey there!'})


def create_entry(request):

    if request.method == 'POST':
        form = HumanForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            h = Human()
            h.name = cd['name']
            h.email = cd['email']
            h.save()
            return HttpResponseRedirect('../list')
    else:
        form = HumanForm()
    return render_form(request, 'create.html', {'form': form})


def list_entries(request):
    humans = Human.objects.all()
    return render_form(request, 'list.html', {'humans': humans})
