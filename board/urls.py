from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('zzap/', views.board_zzap, name='board_zzap'),
    path('create/', views.board_write, name='board_write'),
]