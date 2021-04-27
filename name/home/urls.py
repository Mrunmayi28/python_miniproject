from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index,name='index.html'),
    path('slogin', views.slogin,name='slogin.html'),
    path('plogin', views.logged,name='plogin.html'),
    path('spersonalinfo', views.personalinfo,name='spersonalinfo.html'),
    path('academics', views.student_academics,name='academics.html'),
    path('certifications', views.certifications,name='certifications.html'),
    path('proctor', views.proctor,name='proctor.html'),
    path('succes',views.succes,name='succes.html'),
]
