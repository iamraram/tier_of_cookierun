from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('create/', views.board_write, name='board_write'),
]