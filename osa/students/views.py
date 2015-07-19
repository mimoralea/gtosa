from django.shortcuts import get_object_or_404, render

from .models import Student


def index(request):
    latest_students = Student.objects.all()
    context = {'latest_students': latest_students}
    return render(request, 'students/index.html', context)


def detail(request, student_id):
    latest_students = Student.objects.all()
    student = get_object_or_404(Student, pk=student_id)
    context = {'latest_students': latest_students, 'student': student}
    return render(request, 'students/detail.html', context)
