from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Bb


def home(request):
    template = loader.get_template('landing/index.html')
    bbs = Bb.objects.all()
    context = {
        'bbs': bbs
    }
    return HttpResponse(template.render(context, request))