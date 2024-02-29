from django.urls import path
from .views import detail, new, delete, edit, items, newcategory

app_name = 'Item'

urlpatterns = [
    path('', items, name='items'),
    path('<int:pk>/', detail, name='detail'),
    path('New item/', new, name='newitem'),
    path('New Category/', newcategory, name='newcat'),
    path('<int:pk>/edit/', edit, name='edit'),
    path('<int:pk>/delete/', delete, name='delete'), 
]

