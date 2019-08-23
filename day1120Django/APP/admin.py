# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from APP.models import Students
from APP.models import Grades
from APP.models import Subject
# Register your models here.


# 自定义管理页面
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    # 转换下显示的数据
    def sex_type(self):
        if 'man' == self.sex:
            return '男'
        else:
            return '女'

    sex_type.short_description = '性别'   # 页面数据列的别名

    list_display = ['id', 'name', 'age', 'tel', sex_type, 'birthday']
    list_filter = ['name']
    search_fields = ['name', 'age']
    list_per_page = 5
    # fields = ['name', 'age']
    fieldsets = [
        ('base', {'fields': ['id', 'name', 'age', 'birthday', 'gradeId']}),
        ('other', {'fields': ['tel', 'sex']})
    ]


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ['id', 'classname']
    list_filter = ['id']
    list_per_page = 5
    fields = ['id', 'classname']

# 注册需要管理的表，也可是使用装饰器完成
# admin.site.register(Students, StudentsAdmin)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'sname']
    list_per_page = 5
