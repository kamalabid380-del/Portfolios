from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name='blogs'),
    path('work/', views.home, name='work'),
    path('contact/', views.home, name='contact'),
]
