# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from APP.models import Students, Grades, Subject, Membership
from django.http import HttpResponse

# Create your tests here.


def test(request):
    # gid = Grades.objects.all().get(id=1)
    # print '---------------------------'
    # print gid.classname
    # stu1 = Students(id='100002', name='tom', age=25, tel='18700124945', sex='woman', birthday='2019-07-15 11:12', gradeId=gid)
    # stu1.save()

    # grade = Grades.objects.all().get(id=1)  # 使用主表对象查询从表数据
    # for stu in grade.g_set.all():
    #     print stu.name

    # stu = Students.objects.all().get(id='100001')
    # sub = Subject.objects.all().get(id=3)
    # sub.subjectName.add(stu)
    # for s in stu.subject_set.all():
    #     print s.sname

    # Membership.objects.create(date_join='2019-07-05 10:57', student_id='100001', subject_id=2)
    # for s in stu.subject_set.all():
    #     print s.sname

    stu = Students.objects.filter(id__lt=100003)
    for s in stu:
        print 's:', s.age
    print '---------------------------'
    stu = Students.objects.get(id=100001)
    print stu.age
    return HttpResponse("<p>数据添加成功</p>")





