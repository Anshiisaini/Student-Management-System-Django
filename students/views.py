from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import StudentForm
from .models import Student

def register_user(request):
    if request.user.is_authenticated:
        return redirect('student_list')
    form=UserCreationForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('student_list')
    return render(request,'students/register.html',{'form':form})

@login_required
def student_list(request):
    query=request.GET.get('search','').strip()
    students=Student.objects.all().order_by('name')
    if query:
        students=students.filter(Q(name__icontains=query)|Q(course__icontains=query))
    return render(request,'students/student_list.html',{'students':students,'query':query})

@login_required
def add_student(request):
    form=StudentForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'students/student_form.html',{'form':form,'heading':'Add Student'})

@login_required
def update_student(request,id):
    student=get_object_or_404(Student,id=id)
    form=StudentForm(request.POST or None,instance=student)
    if request.method=='POST' and form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'students/student_form.html',{'form':form,'heading':'Update Student'})

@login_required
def delete_student(request,id):
    student=get_object_or_404(Student,id=id)
    if request.method=='POST':
        student.delete()
        return redirect('student_list')
    return render(request,'students/delete_student.html',{'student':student})
