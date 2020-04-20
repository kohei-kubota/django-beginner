from django.contrib import admin
from .models import TodoModel

admin.site.register(TodoModel) # model.pyで指定した関数
