from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('newpost', views.newpost, name='newpost'),
    path('blog/<str:pk>', views.blog, name='post'),
    path('all', views.all, name='all'),
    path('user/<str:pk>', views.user, name='user'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('search', views.search, name='search')
]