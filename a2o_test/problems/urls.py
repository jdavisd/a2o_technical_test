from django.urls import path
from problems import views

app_name = 'problems'

urlpatterns = [
    path('problem1/', views.problem1,name='problem1'),
    path('problem2/', views.problem2,name='problem2'),
]
