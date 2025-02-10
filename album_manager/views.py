from django.http import HttpResponse
from django.template import loader
from .models import Artist, Album
from album_manager.forms import ArtistForm, AlbumForm
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView


def index(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'artists': artists, 'albums' : albums}, request))



def edit_artist(request, artist_id):
    artist = Artist.objects.get(pk = artist_id)
    if request.method == "POST":
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = ArtistForm(instance=artist)
        
    return render(request, 'artist_form.html', {'form': form})


def delete_artist(request, artist_id):
    artist = Artist.objects.get(pk = artist_id)
    artist.delete()
    return redirect('album_manager:index')





def edit_album(request, album_id):
    album = Album.objects.get(pk = album_id)
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_manager:index')
    else:
        form = AlbumForm(instance=album)
        
    return render(request, 'album_form.html', {'form': form})


def delete_album(request, album_id):
    album = Album.objects.get(pk = album_id)
    album.delete()
    return redirect('album_manager:index')
def artist(request, artist_id):
    artist = Artist.objects.get(pk = artist_id)
    template = loader.get_template('display_artist.html')
    context = {
        'artist': artist
    }
    return HttpResponse(template.render(context, request))


def album(request, album_id):
    album = Album.objects.get(pk = album_id)
    template = loader.get_template('display_album.html')
    context = {
        'album': album
    }
    return HttpResponse(template.render(context, request))


def show_artists(request):
    artists = Artist.objects.all()
    template = loader.get_template('only_artist.html')
    return HttpResponse(template.render({'artists': artists}, request))


def show_albums(request):
    albums = Album.objects.all()
    template = loader.get_template('only_album.html')
    return HttpResponse(template.render({'albums' : albums}, request))



