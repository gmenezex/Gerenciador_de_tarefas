from django.contrib import admin
from todolist.models import Todo, Status

class TodoAdmin(admin.ModelAdmin):
  list_display = ('task','status','date')
  search_fields = ('task',)


class StatusAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

admin.site.register(Todo, TodoAdmin)
admin.site.register(Status, StatusAdmin)