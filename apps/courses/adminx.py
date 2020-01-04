#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wukong'
__date__ = '2018/3/15 21:57'

import xadmin
from .models import *
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree',
                    'learn_times', 'students', 'add_time', 'get_zj_nums', 'go_to']
    list_filter = ['name', 'desc', 'degree',
                   'learn_times', 'students', 'add_time']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students']

    ordering = ['-add_time']
    model_icon = 'fa fa-apple'
    readonly_fields = ['add_time']
    exclude = ['degree']
    list_editable = ['degree', 'desc']
    refresh_times = [5, 10]
    relfield_style = 'fk-ajax'

    inlines = [LessonInline]

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerCourseAdmin(object):
    list_display = ['name', 'desc', 'degree',
                    'learn_times', 'students', 'add_time', 'get_zj_nums', 'go_to']
    list_filter = ['name', 'desc', 'degree',
                   'learn_times', 'students', 'add_time']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students']

    ordering = ['-add_time']
    model_icon = 'fa fa-apple'
    readonly_fields = ['add_time']
    exclude = ['degree']
    list_editable = ['degree', 'desc']
    refresh_times = [5, 10]
    relfield_style = 'fk-ajax'

    inlines = [LessonInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    list_filter = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    list_filter = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
