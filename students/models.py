from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Department(models.Model):
    name=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name

class StudentDepartment(models.Model):
    student=models.OneToOneField(Student,on_delete=models.CASCADE,related_name='department_assignment')
    department=models.ForeignKey(Department,on_delete=models.PROTECT,related_name='student_assignments')
    def __str__(self):
        return f'{self.student.name} - {self.department.name}'
