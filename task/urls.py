from django.urls import path, include
from .views import TasksListView
urlpatterns = [
    path('', TasksListView.as_view(), name="tasks-list")
]
