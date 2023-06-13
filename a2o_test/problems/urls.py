from django.urls import path
from problems import views

app_name = 'problems'

urlpatterns = [
    path('problem-1/', views.problem1,name='problem1'),
    path('problem-2/', views.problem2,name='problem2'),
]
