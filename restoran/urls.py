from django.urls import path
from restoran import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('menu/', views.menu, name='menu'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.ourteam, name='ourteam'),
    path('testimonial/', views.testmonial, name='testimonial'),

]

