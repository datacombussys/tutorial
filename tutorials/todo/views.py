from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Todo, ItemsTodo
from django.views import View
from .forms import TodoForm, ItemsTodoForm

# Create your views here.

class Todo_Index(View):
	template = 'todo/index.html'
	form = TodoForm
	def get(self, request):
		return render(request, 'todo/index.html', {
			"todos": Todo.objects.all(),
			'form': self.form(),
		})

	def post(self, request):
		print(request.POST)
		form = self.form(request.POST)
		if form.is_valid():
			form.save()

			return redirect('todo:index')

		else:
			context = {
				'form' : form,
				'todos' : Todo.objects.all()
			}

			return render(request, self.template, context)

class Todo_Detail(View):
	template = 'todo/detail.html'
	form = ItemsTodoForm
	def get(self, request, todo_id):
		try:
			todo_object = Todo.objects.get(pk=todo_id)

			context = {
				'todo_object' : todo_object,
				'form' : self.form(),
			}
		except Todo.DoesNotExist:
			raise Http404("Does Not exist. Please try again")
		except KeyError:
			raise Http404("KeyError")

		return render(request, self.template, context)

	def post(self, request, todo_id):
		'''We need to be able to link the foreign key 
		"todo_list" to the current page and pass 
		it to the POST request. We need to modify the
		ItemsTodoForm to include the PK.
		When we submit the form, the system does not know what 
		list (pk) to attach the items to.
		'''
		ItemsTodoForm['todo_list'] == todo_id
		form = self.form(request.POST)
		if form.is_valid():
			form.save()

			return redirect('todo:detail', todo_id)

		else:
			todo_object = Todo.objects.get(pk=todo_id)
			context = {

				'form' : form,
				'todo_object' : todo_object,
			}

			return render(request, self.template, context)

	