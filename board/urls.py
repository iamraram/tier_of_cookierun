from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path('zzap/', views.board_zzap, name='board_zzap'),
    path('create/', views.board_write, name='board_write'),
    path('delete/<int:question_id>/', views.board_delete, name='board_delete'),
    path('modify/<int:question_id>/', views.board_modify, name='board_modify'),
]