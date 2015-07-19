from django.shortcuts import get_object_or_404, render

from .models import Specialization


def index(request):
    latest_specializations = Specialization.objects.all()
    context = {'latest_specializations': latest_specializations}
    return render(request, 'specializations/index.html', context)


def detail(request, specialization_id):
    latest_specializations = Specialization.objects.all()
    specialization = get_object_or_404(Specialization, pk=specialization_id)
    context = {'latest_specializations': latest_specializations,
               'specialization': specialization}
    return render(request, 'specializations/detail.html', context)
