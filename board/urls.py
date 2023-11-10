from django.urls import path
from . import views

from django.views.defaults import page_not_found

urlpatterns = [
    path('', views.index),
    path('<int:question_id>/', views.detail),
    path(page_not_found, views.notfound)
]