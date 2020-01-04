#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wukong'
__date__ = '2018/3/15 22:43'

import xadmin
from .models import *


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']



class CourseOrgAdmin(object):
    list_display = ['name', 'fav_nums', 'city', 'add_time']
    list_filter = ['name', 'fav_nums', 'city', 'add_time']
    search_fields = ['name', 'fav_nums', 'city']


class TeacherAdmin(object):
    list_display = ['name', 'work_years',
                    'work_company', 'work_position', 'add_time']
    list_filter = ['name', 'work_years',
                   'work_company', 'work_position', 'add_time']
    search_fields = ['name', 'work_years', 'work_company', 'work_position']


xadmin.site.register(CityDict, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
