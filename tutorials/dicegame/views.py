from django.shortcuts import render
from django.views import View, generic



# Create your views here.

class IndexPage(generic.ListView):
	template_name = 'dicegame/index.html'


    