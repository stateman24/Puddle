from django.urls import path 
from .views import index

app_name = 'Dashboard'

urlpatterns = [
    path('', index, name='dashboard'),
]
