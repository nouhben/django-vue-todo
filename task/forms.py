from django.forms.models import ModelForm
from .models import Task
class TaskForm(ModelForm):
    model = Task
    fields = ['title']