from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('feature', views.feature, name='feature'),
    path('team', views.team, name='team'),
    path('menu', views.menu, name='menu'),
    path('booking', views.book, name='booking'),
    path('blog', views.blog, name='blog'),
    path('single', views.detail, name='detail'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register')
]