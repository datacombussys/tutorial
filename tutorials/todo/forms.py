from django.forms import ModelForm
from .models import Todo, ItemsTodo

class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['name', 'is_completed']

class ItemsTodoForm(ModelForm):
	class Meta:
		model = ItemsTodo
		fields = ['name', 'is_completed', 'todo_list']
		# exclude = ['todo_list']