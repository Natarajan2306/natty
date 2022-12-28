from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

from .forms import DatabaseForm

from .filters import DatabaseFilter

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages



# Create your views here.



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

	

	