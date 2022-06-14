from django.contrib import admin
from .models import *

class CityAdmin(admin.ModelAdmin):
	list_display = ('country', 'city', 'iso', 'time_zone')

admin.site.register(City, CityAdmin)