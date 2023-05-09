from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bb
from .models import Rubric
from .forms import BbForm


def home(request):
    # template = loader.get_template('landing/index.html')
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'items': bbs,
        'rubrics': rubrics,
        'mail': 'info@flowersandtoys.ru',
        'address': 'Москва, ул. Первомайская д. 100',
        'phones': ['+79914025052'
                   '+79990955411']
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

    return render(request, 'landing/goods.html', context)




class BbCreateView(CreateView):
    template_name = 'landing/create.html'
    form_class = BbForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
