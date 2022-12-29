import django_filters
from django_filters import CharFilter

from .models import *

class DatabaseFilter(django_filters.FilterSet):
	companies = CharFilter(field_name='companies')
	first_name = CharFilter(field_name='first_name')
	last_name = CharFilter(field_name='last_name')
	Title = CharFilter(field_name='Title')
	email = CharFilter(field_name='email')
	
	class Meta:
		model  = Database
		fields = ('companies', 'first_name', 'last_name', 'Title', 'email')