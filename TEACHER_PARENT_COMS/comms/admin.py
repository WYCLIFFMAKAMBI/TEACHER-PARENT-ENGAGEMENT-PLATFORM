from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role')
    list_filter = ('role',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(events)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Assignments)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'title',)
    search_fields = ('subject', 'title',)

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('year',)
    search_fields = ('year',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'session', 'student_class',)
    search_fields = ('name', 'session__year', 'student_class__class_name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'admission_no', 'session', 'student_class',)
    search_fields = ('student_name', 'admission_no', 'session__year', 'student_class__class_name',)

@admin.register(StudentClass)
class StudentClassAdmin(admin.ModelAdmin):
    list_display = ('class_name',)
    search_fields = ('class_name',)

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'grade',)
    search_fields = ('student__student_name', 'subject__name',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'is_present',)
    list_filter = ('date', 'is_present',)
    search_fields = ('student__student_name',)


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ['user', 'student_name']
    search_fields = ['user__username', 'student_name']

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', 'tsc_no']
    search_fields = ['user__username', 'tsc_no']

admin.site.register(Studentprofile)