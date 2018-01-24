from django.db import models
from django.urls import reverse
# Create your models here.
'''
 3 steps to install the update
 python3 manage.py makemigrations music
 python3 manage.py sqlmigrate music 0001
 python3 manage.py migrate
 activate shell python3 manage.py shell
 get all: Album.objects.all()  [running in shell]
 after add filed remember to xx.save()
'''



class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' - ' + self.artist


''' add song 
 #1 album1.song_set.create(song_title='lucky', file_type='mp3')
 #2
     song = Song()
     song.album = album1
     song.file_type = 'mp3'
     song.song_title = 'i hate my boyfriend'
     song.save()
     Song.objects.all() 
'''
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
        
    