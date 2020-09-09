from django.urls import path
from .views import viewhygio

urlpatterns = [
    path('',viewhygio,name='viewhygio')    # path('add', add_note, name='add_note'),
]
