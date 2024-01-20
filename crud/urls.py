from django.contrib import admin
from django.urls import path
from .views import *        #can use * to import all



urlpatterns = [
    #adddata
    path('add-student/',StudentView.post_student),
    path('add-teacher/',TeacherView.post_teacher),
    #fetchdata
    path('get-student/',getStudent),
    path("get-teacher/",getTeacher),
    #edit data
    path("edit-student/<id>",UpdateStudent),
    path("edit-teacher/<id>",UpdateTeacher),
    path("Delete-Student/<id>",DeleteStudent)
]
