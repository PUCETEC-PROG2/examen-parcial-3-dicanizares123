from django.urls import path

from . import views

app_name = 'album_manager'

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:album_id>/", views.album, name="album"),
    path("artist/<int:artist_id>/", views.artist, name="artist"),
    path("show_albums/", views.show_albums, name="show_albums"),
    path("show_artists/", views.show_artists, name="show_artists"),
    path("edit_artist/<int:artist_id>/", views.edit_artist, name="edit_artist"),
    path("delete_artist/<int:artist_id>/", views.delete_artist, name="delete_artist"),
    path("edit_album/<int:album_id>/", views.edit_album, name="edit_album"),
    path("delete_album/<int:album_id>/", views.delete_album, name="delete_album")
   
]