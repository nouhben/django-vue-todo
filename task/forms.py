from django.forms.models import ModelForm
from task.models import Task
class TaskForm(ModelForm):
    model = Task
    fields = ['title']