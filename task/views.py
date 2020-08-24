from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
class TasksListView(ListView):
    def get(self,request):
        return render(request,'task/tasks.html',context={'name':'BALCK & WHITE'})