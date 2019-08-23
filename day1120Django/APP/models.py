# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# Create your models here.


class Grades(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='编号')
    classname = models.CharField(max_length=36, verbose_name='班级')

    def __str__(self):
        return self.classname

    class Meta:
        db_table = 'grades'
        ordering = ['id']


class Students(models.Model):
    id = models.IntegerField(max_length=6, primary_key=True, verbose_name='学号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    age = models.CharField(max_length=3, verbose_name='年龄')
    tel = models.CharField(max_length=11, verbose_name='电话')
    sex = models.CharField(max_length=10, verbose_name='性别')
    birthday = models.DateTimeField(verbose_name='生日')
    gradeId = models.ForeignKey('Grades', related_name='g_set', db_column='gradeid')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'
        ordering = ['id']


class Subject(models.Model):
    id = models.IntegerField(max_length=6, primary_key=True, verbose_name='科目编号')
    sname = models.CharField(max_length=32)
    subjectName = models.ManyToManyField(Students, through='Membership')

    def __str__(self):
        return self.sname

    class Meta:
        db_table = 'subject'


class Membership(models.Model):
    student = models.ForeignKey(Students)
    subject = models.ForeignKey(Subject)
    date_join = models.DateTimeField()

    class Meta:
        db_table = 'membership'


