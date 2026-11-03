from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('work/', views.work, name='work'),
    path('work/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blogs/', views.blog, name='blogs'),
    path('blogs/<slug:slug>/', views.blog_post, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    path('contact/sent/', views.contact_sent, name='contact_sent'),
    path('robots.txt', views.robots, name='robots'),
]
