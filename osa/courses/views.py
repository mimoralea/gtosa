from django.shortcuts import get_object_or_404, render

from .models import Course


def index(request):
    latest_courses = Course.objects.all()
    context = {'latest_courses': latest_courses}
    return render(request, 'courses/index.html', context)


def detail(request, course_id):
    latest_courses = Course.objects.all()
    course = get_object_or_404(Course, pk=course_id)
    context = {'latest_courses': latest_courses, 'course': course}
    return render(request, 'courses/detail.html', context)
