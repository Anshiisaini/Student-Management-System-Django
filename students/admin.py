from django.contrib import admin
from .models import Student,Department,StudentDepartment
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(StudentDepartment)
