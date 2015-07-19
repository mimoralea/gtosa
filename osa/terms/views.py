from django.shortcuts import get_object_or_404, render

from .models import Term


def index(request):
    latest_terms = Term.objects.all()
    context = {'latest_terms': latest_terms}
    return render(request, 'terms/index.html', context)


def detail(request, term_id):
    latest_terms = Term.objects.all()
    term = get_object_or_404(Term, pk=term_id)
    context = {'latest_terms': latest_terms, 'term': term}
    return render(request, 'terms/detail.html', context)
