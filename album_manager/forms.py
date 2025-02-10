from django import forms
from .models import Artist, Album

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = '__all__'
        labels = {
            'artist_name': 'Nombre del Artista',
            'country': 'Pais de Origen',
            'picture': 'Foto del Artista',
            
        }
        widgets = {
            'artist_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'picture':forms.ClearableFileInput(attrs={'class': 'form-control'})
        }
        
class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'title': 'Título del Álbum',
            'realase_year': 'Año de Lanzamiento',
            'genre': 'Género',
            'artist': 'Artista',
            'cover': 'Portada'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'realase_year': forms.DateInput(
                attrs={
                    'class': 'form-control', 
                    'type': 'date',  # HTML5 date picker
                }
            ),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'artist': forms.Select(attrs={'class': 'form-control'}),
            'cover': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }