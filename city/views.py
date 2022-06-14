from django.shortcuts import render
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from .models import *

class HomePageView(TemplateView):
	template_name = 'home.html'

class SearchView(ListView):
	model = City
	template_name = 'search_results.html'

	def get_queryset(self):
		query = self.request.GET.get("q")
		object_list = City.objects.filter(
			Q(country__icontains=query) | Q(iso__icontains=query)
			)
		return object_list