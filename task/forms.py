from django.forms import models
from task.models import Task
class TaskForm(models.ModelForm):
    model = Task
    fields = ['title']