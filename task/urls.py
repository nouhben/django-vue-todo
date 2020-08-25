from django.urls import path, include
from .views import TaskView, TaskDone,TaskDelete
urlpatterns = [
    path('', TaskView.as_view(), name="tasks-list"),
    path('<str:id>/done/', TaskDone.as_view(), name="task-done"),
    path("<str:id>/delete/", TaskDelete.as_view(), name="task-delete"),
]
