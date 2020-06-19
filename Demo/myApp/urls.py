from django.urls import path
from. import views

urlpatterns = [
    path('index/', views.index),
    path('attributes/', views.attributes),
    path('get1', views.get1),
    path('get2', views.get2),
    path('register', views.register),
    path('showregister', views.showregister),
    path('students/', views.students),
    path('verifycode/',views.verifycode),
    
    path('upfile/', views.upfile),
    path('savefile', views.savefile),

    path("studentpage/<int:pageid>", views.studentpage),
]

