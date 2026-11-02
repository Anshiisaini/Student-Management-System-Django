from django.urls import path
from django.contrib.auth import views as auth_views
from . import views,api_views
urlpatterns=[
    path('',views.student_list,name='home'),
    path('students/',views.student_list,name='student_list'),
    path('add-student/',views.add_student,name='add_student'),
    path('update-student/<int:id>/',views.update_student,name='update_student'),
    path('delete-student/<int:id>/',views.delete_student,name='delete_student'),
    path('register/',views.register_user,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='students/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('api/students/',api_views.StudentListCreateAPI.as_view(),name='api_student_list'),
    path('api/students/<int:pk>/',api_views.StudentDetailAPI.as_view(),name='api_student_detail'),
]
