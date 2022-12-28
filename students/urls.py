
from django.urls import path
from . import views




urlpatterns = [
    path('Register/', views.registerpage, name='Register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),



    path('', views.home, name='home'),
    path('students/', views.student_data, name='students'),
    path('create_student/', views.create_Student, name='create_student')
    

]
	