from django.urls import path
from .views import list, show, add, update, activate, delete

urlpatterns = [
    path('', list, name='list'),
    path('<int:blacklist_id>', show, name='show'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('activate/<int:blacklist_id>', activate, name='activate'),
    path('delete/<int:blacklist_id>', delete, name='delete'),
]