from django.db import models

# Create your models here.
class Task(models.Model):
    TASK_STATUS = [
        ('done','todo'),('todo','todo'),('deleted','deleted'),
    ]
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    #status = models.CharField(max_length=50,choices=TASK_STATUS)
    isDone = models.BooleanField(default=False)
    class Meta:
        ordering = ['isDone','created']