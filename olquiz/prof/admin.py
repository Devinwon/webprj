from django.contrib import admin
from .models import StudentProfile, TeacherProfile
from django.db import models


class StudentProfileAdmin(admin.ModelAdmin):
	list_display = ['user','date_of_birth','gender']


class TeacherProfileAdmin(admin.ModelAdmin):
	list_display = ['user','date_of_birth','gender']


admin.site.register(StudentProfile,StudentProfileAdmin)
admin.site.register(TeacherProfile,TeacherProfileAdmin)