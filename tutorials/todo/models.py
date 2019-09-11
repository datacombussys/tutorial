from django.db import models

# Create your models here.

class Todo(models.Model):
	# Define Fields Here
	name = models.CharField(max_length=200)
	is_completed = models.BooleanField(default=False)
	added_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


class ItemsTodo(models.Model):
	name = models.CharField(max_length=200)
	is_completed = models.BooleanField(default=False)
	added_date = models.DateField(auto_now_add=True)
	todo_list = models.ForeignKey(Todo, on_delete=models.CASCADE, null=False)

	def __str__(self):
		return self.name
