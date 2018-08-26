from django.urls import path
from . import views

urlpatterns = [
    path('dupa', views.post_list, name='post_list'),
]

