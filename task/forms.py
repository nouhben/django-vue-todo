from django.forms import models
from task.models import Task
class TaskForm(models.ModelForm):
    class Meta:
        model = Task
        fields = ['title']