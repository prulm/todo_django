from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from .models import *
from .serializers import *

class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteUpdateView(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteGetView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDeleteView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    