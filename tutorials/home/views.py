from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

class Poll_View(View):
	def get(self, request):
		return render(request, 'home/index.html')