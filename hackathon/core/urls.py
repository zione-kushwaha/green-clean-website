from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('awareness/', views.aware, name='awareness'),

    path('posts/', views.post, name='post'),
]
