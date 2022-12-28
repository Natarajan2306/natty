from django.db import models

# Create your models here.
class Database(models.Model):
	companies = models.CharField(max_length=100, null=True)
	first_name = models.CharField(max_length=300, null=True)
	#enrollment_year = models.IntegerField(null=True)
	last_name = models.CharField(max_length=100, null=True)
	#phone_number = models.CharField(max_length=100, null=True)
	Title = models.CharField(max_length=100, null=True)
	email = models.EmailField(max_length=100, null=True)
	url = models.CharField(max_length=100, null=True)
	#completion_year = models.IntegerField(null=True)

	def __str__(self):
		return self.last_name