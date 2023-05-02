from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Bb
from .models import Rubric


def home(request):
    # template = loader.get_template('landing/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics
    }
    return render(request, 'landing/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'bbs': bbs,
        'current_rubric': current_rubric,
        'rubrics': rubrics
    }

    return render(request, 'landing/by_rubric.html', context)
