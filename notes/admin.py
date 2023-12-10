from django.contrib import admin
from .models import *

class NotesAdmin(admin.ModelAdmin):
    list_display = ('id', 'content','created_on','updated_on')
    list_display_links = ('id', 'content')
    search_fields = ('content')

admin.site.register(Note)
