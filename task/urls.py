from django.urls import path, include
from .views import TaskView, TaskDone
urlpatterns = [
    path('', TaskView.as_view(), name="tasks-list"),
    path('<str:id>/done/', TaskDone.as_view(), name="tasks-done")
]
