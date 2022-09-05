from django.urls import path
from . import views

app_name = 'loginpage'

urlpatterns = [
    path('', views.index),
    path('student_registration_save/', views.student_registration_save, name='student_registration_save')
]