from django.urls import path
from . import views


urlpatterns = [
    path('', views.archive, name='archive'),
    path('create', views.create_blogpost, name='create'),
]
