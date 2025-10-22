from django.db import models

class Status(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Todo(models.Model):
  id = models.AutoField(primary_key=True)
  task = models.CharField(max_length=300)
  status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='status_todo')
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.task
