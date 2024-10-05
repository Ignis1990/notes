from django.urls import path

from .views import index, get_note, create_note, update_note

urlpatterns = [
    path('', index, name='index'),
    path('notes/<int:pk>/', get_note, name='note'),
    path('create/', create_note, name='create'),
    path('update/<int:pk>/', update_note, name='update'),
]
