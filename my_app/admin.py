from django.contrib import admin
from .models import ToDo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(ToDo, TodoAdmin)