from django.urls import path
from .views import list, show, add, update, activate, delete

urlpatterns = [
    path('', list, name='list'),
    path('<int:bis_id>', show, name='show'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('activate/<int:bis_id>', activate, name='activate'),
    path('delete/<int:bis_id>', delete, name='delete'),
]