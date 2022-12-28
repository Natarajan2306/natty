from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

from .forms import DatabaseForm,CreateUserForm

from .filters import DatabaseFilter

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required






# Create your views here.

def registerpage(request):
	if request.user.is_authenticated:
		return redirect('home')
		
	else:	
			form = CreateUserForm()
			if request.method == 'POST':
				form = CreateUserForm(request.POST)
				if form.is_valid():
					form.save()
					user = form.cleaned_data.get('username')
					messages.success(request, 'Account was created for' + user)
					return render(request, '/Users/hysntechnologies/Downloads/import/student_database/students/templates/login.html')


				
				
			
			context = {'form':form}
			return render(request, '/Users/hysntechnologies/Downloads/import/student_database/students/templates/Register.html', context)

def loginpage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
			if request.method == 'POST':
				username = request.POST.get('username')
				password = request.POST.get('password')
				user = authenticate(request ,username=username, password = password)

				if user is not None:
					login(request ,user)
					return redirect('home')
				else:
					messages.info(request, 'Username or Password is incorrect')



			context = {}
			return render(request, '/Users/hysntechnologies/Downloads/import/student_database/students/templates/login.html', context)

		    
	
def logoutUser(request):
	logout(request)
	messages.info(request, 'you have logout successfully')
	return redirect('login')

@login_required(login_url='login')


def home(request):

	students = Database.objects.all()

	total_students = students.count()

	total_courses = Database.objects.values('companies').distinct().count()

	context = {'total_students' : total_students, 'total_courses': total_courses}


	return render(request, 'students/dashboard.html', context )

def student_data(request):

	students = Database.objects.all()

	myFilter = DatabaseFilter(request.GET, queryset=students)

	students = myFilter.qs




	context = {'students' : students, 'myFilter' : myFilter}

	return render(request, 'students/students.html', context)
@login_required(login_url='login')


def create_Student (request):

	form = DatabaseForm
	if request.method == 'POST':
		# print('printing POST', request.POST)
		form = DatabaseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')


	context = {'form' : form}

	return render(request, 'students/student_form.html', context)

	

	