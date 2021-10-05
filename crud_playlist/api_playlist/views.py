from api_playlist.models import Playlist, Music, Artist
from rest_framework import viewsets
from rest_framework import permissions
from api_playlist.serializers import PlaylistSerializer, MusicSerializer, ArtistSerializer

class PlaylistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Playlist.objects.all().order_by('-date_joined')
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticated]


class MusicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated]

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticated]


