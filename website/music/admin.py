from django.contrib import admin
from .models import Album, Song

# Register your models here.

'''
creating admin account: python3 manage.py createsuperuser

'''

admin.site.register(Album)
admin.site.register(Song)