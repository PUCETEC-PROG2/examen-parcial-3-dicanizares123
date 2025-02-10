from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=30, null=False)
    country = models.CharField(max_length=30, null=False)
    picture = models.ImageField(upload_to="artist_images")
    
    def _str_(self) -> str:
        return f'{self.artist_name} {self.country}'


class Album(models.Model):
    title = models.CharField(max_length=30, null=False)
    realase_year = models.DateField()
    ALBUM_GENRE = {
        ('R', 'Rock'),
        ('C', 'Clásico'),
        ('P', 'Pop'),
        ('E', 'Eléctronica'),
        ('O', 'Otro')
    }
    genre = models.CharField(max_length=30, choices=ALBUM_GENRE, null=False)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    cover = models.ImageField(upload_to="album_images")
    
    def _str_(self):
        return self.title