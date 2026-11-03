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
    path('ahrefs_e57b5e9d5d7d1aee1162f6dbc71c50e6c1e8051f398cc2551e045d0ec998462d',
         views.ahrefs_verify, name='ahrefs_verify'),
    path('ahrefs_e57b5e9d5d7d1aee1162f6dbc71c50e6c1e8051f398cc2551e045d0ec998462d.html',
         views.ahrefs_verify, name='ahrefs_verify_html'),
]
