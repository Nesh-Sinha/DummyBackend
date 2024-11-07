from django.urls import path
from . import views

urlpatterns = [
    path('save_name/', views.save_name, name='save_name'),
]
