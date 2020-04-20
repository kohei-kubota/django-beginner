from django.contrib import admin
from django.urls import path, include
from .views import helloworld, HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', helloworld),
    path('test2/', HelloWorld.as_view()),
    path('hello/', include('helloworldapp.urls'))
]
