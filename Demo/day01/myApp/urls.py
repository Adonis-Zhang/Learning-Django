from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),

    path('<int:question_id>/<int:question_id2>/', views.detail, name='detail'),
    
    path('grades/', views.grades),
    path('stu/', views.Stu),

    path('addStu/', views.addStu),
    path('addStu2/', views.addStu2),


    path('showStu/', views.showStu),
    path('showStu/<int:page>/', views.showStuPage, name='showStuPage'),

    path('studentsearch/', views.studentsearch),


]

