from django.contrib import admin

from .models import Student, Teacher


class StudentInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 1

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'group']
    filter_horizontal = ['teachers']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ['name', 'subject']
    list_filter = ['subject']


