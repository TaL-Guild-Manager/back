from django.urls import path
from .views import list, show, find, add, update, activate, delete

urlpatterns = [
    path('', list, name='list'),
    path('<int:member_id>', show, name='show'),
    path('find', find, name='find'),
    path('add', add, name='add'),
    path('update', update, name='update'),
    path('activate/<int:member_id>', activate, name='activate'),
    path('delete/<int:member_id>', delete, name='delete'),
]