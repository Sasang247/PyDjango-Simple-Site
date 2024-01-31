from django.urls import path
from .import views

urlpatterns = [


    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('services/',views.services,name='services'),
    path('joinus/',views.joinus,name='joinus'),
    path('blog/',views.blog,name='blog'),
    path('about/',views.about,name='about'),
    path('buildwithus/',views.buildwithus,name='buildwithus'),
    path('carrers/',views.carrers,name='carrers'),
    path('internship/',views.internship,name='internship'),
    path('apply/',views.apply,name='apply')

]
