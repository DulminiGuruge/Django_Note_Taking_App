from django.contrib import admin
from . import models

# Register your models here.
class NoteAdmin(admin.ModelAdmin):#inherit from admin.ModelAdmin
    #to display the notes by title in the admin interface
    list_display = ('title',)

admin.site.register(models.Notes, NoteAdmin) #nodeadmin is attached to the admin model