from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher, StudentTeacher


def students_list(request):
    template = 'school/students_list.html'
    context = Student.objects.prefetch_related('teacher').all()
    context = {'object_list': context}


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
