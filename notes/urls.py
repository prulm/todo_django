from django.urls import path
from .views import *

urlpatterns = [
	path('create/', NoteCreateView.as_view(), name='create-note'),
	path('load/', NoteGetView.as_view(), name='load-notes'),
	path('update/', NoteUpdateView.as_view(), name='update-note'),
	path('delete/<int:pk>/', NoteDeleteView.as_view(), name='delete-note'),
]