from django.shortcuts import render,redirect
from django.views.generic import ListView, View
from django.http import JsonResponse

# Create your views here.
from .models import  Task
from .forms import TaskForm
from django.forms.models import model_to_dict 
#to serialize a model instance to json 

class TaskView(View):

    def get(self,request):
        _tasks = list(Task.objects.all().values()) 
        #Convert the values of the queryset to a list of dict
        if request.is_ajax():
            return JsonResponse({'tasks':_tasks}, status=200)
        return render(request,'task/tasks.html')

    def post(self,request):
        bound_form = TaskForm(request.POST)
        if bound_form.is_valid():
            new_task = bound_form.save()
            return JsonResponse({'newTask':model_to_dict(new_task)}, status=200)
        return redirect('tasks-list')

class TaskDone(View):

    def post(self,request, id):
        taskCompleted = Task.objects.get(id=id)
        taskCompleted.isDone = True
        taskCompleted.save()
        return JsonResponse({'taskCompleted':model_to_dict(taskCompleted)},status=200)