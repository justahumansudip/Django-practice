from django.contrib import admin
from django.urls import path
from .views import StudentView                #can use * to import all



urlpatterns = [
    path('add-student/',StudentView.post_student),
]
