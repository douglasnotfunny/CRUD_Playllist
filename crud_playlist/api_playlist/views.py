from api_playlist.models import Playlist, Music, Artist
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView
from api_playlist.serializers import PlaylistSerializer, MusicSerializer, ArtistSerializer

#PLAYLIST CRUD
class DeletePlaylistAPIView(DestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class ListPlaylistAPIView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class UpdatePlaylistAPIView(UpdateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


# MUSIC CRUD
class DeleteMusicAPIView(DestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class ListMusicAPIView(ListAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class UpdateMusicAPIView(UpdateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


# ARTIST CRUD
class DeleteArtistAPIView(DestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ListArtistAPIView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class UpdateArtistAPIView(UpdateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


