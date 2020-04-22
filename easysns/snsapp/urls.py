from django.urls import path, include
from .views import signup, signin, pagefunc, logoutfunc, detailfunc, goodfunc, readfunc

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('page/', pagefunc, name='page'),
    path('logout/', logoutfunc, name='logout'),
    path('detail<int:pk>', detailfunc, name='detail'),
    path('good<int:pk>', goodfunc, name='good'),
    path('read<int:pk>', readfunc, name='read'),
]
