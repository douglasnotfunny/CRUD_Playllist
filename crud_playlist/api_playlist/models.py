from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    date_joined = models.DateField(auto_now_add=True, blank=True)
    
    class Meta:
        ordering = ['name']


class Music(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True, blank=True)
    
    class Meta:
        ordering = ['name']
        


class Playlist(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    date_joined = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['name']
         