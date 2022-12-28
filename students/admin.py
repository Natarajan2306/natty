from django.contrib import admin

# Register your models here.

from .models import Database

# admin.site.register(Student)

from import_export.admin import ImportExportModelAdmin

@admin.register(Database)


class ViewAdmin(ImportExportModelAdmin):
	pass
