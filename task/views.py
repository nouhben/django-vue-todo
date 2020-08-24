from django.shortcuts import render
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.
from .models import  Task
from .forms import TaskForm
class TasksListView(ListView):
    
    def get(self,request):
        tasks_qs = Task.objects.all()
        _tasks = list(tasks_qs.values())
        #return render(request,'task/tasks.html',context={'name':'BALCK & WHITE'})
        return JsonResponse({'tasks':_tasks}, status=200,safe=False)