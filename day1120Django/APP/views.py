# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Students


def index(request):
    stu_list = Students.objects.all()
    return render(request, 'APP/students.html', {"students": stu_list})
