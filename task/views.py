from django.shortcuts import render,redirect
from django.views.generic import ListView, View
from django.http import JsonResponse

# Create your views here.
from .models import  Task
from .forms import TaskForm
from django.forms.models import model_to_dict

class TaskView(View):
    
    def get(self,request):
        tasks_qs = Task.objects.all()
        _tasks = list(tasks_qs.values()) #Convert the values of the queryset to a list of dict
        if request.is_ajax():
            return JsonResponse({'tasks':_tasks}, status=200, safe=False)
        return render(request,'task/tasks.html',context={'name':'BALCK & WHITE'})

    def post(self,request):
        bounded_form = TaskForm(request.POST)

        if bounded_form.is_valid():
            new_task = bounded_form.save()
            return JsonResponse({'task':model_to_dict(new_task)}, status=200,safe=False)
        return redirect('tasks-list')