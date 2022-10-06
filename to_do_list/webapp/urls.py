from django.contrib import admin
from django.urls import path
from webapp.views.base import IndexView
from webapp.views.tasks import TaskCreateView




urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', TaskCreateView.as_view(), name='create_task')
]