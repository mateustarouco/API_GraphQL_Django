from django.db import models

class MusicsModel(models.Model):
    name = models.CharField(max_length=50)
    albun = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
