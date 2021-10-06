"""crud_playlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api_playlist import views
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'playlist', views.PlaylistViewSet)
router.register(r'music', views.MusicViewSet)
router.register(r'artist', views.ArtistViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls), name='users'),
    # Playlists CRUD
    path("playlist/", views.ListPlaylistAPIView.as_view(),name="playlist_list"),
    path("playlist/update/<int:pk>", views.UpdatePlaylistAPIView.as_view(),name="playlist_update"),
    path("playlist/delete/<int:pk>", views.DeletePlaylistAPIView.as_view(),name="playlist_delete"),  

    # Music CRUD  
    path("music/", views.ListMusicAPIView.as_view(),name="music_list"),
    path("music/update/<int:pk>", views.UpdateMusicAPIView.as_view(),name="music_update"),
    path("music/delete/<int:pk>", views.DeleteMusicAPIView.as_view(),name="music_delete"),  

    # Artist CRUD  
    path("artist/", views.ListArtistAPIView.as_view(),name="artist_list"),
    path("artist/update/<int:pk>", views.UpdateArtistAPIView.as_view(),name="artist_update"),
    path("artist/delete/<int:pk>", views.DeleteArtistAPIView.as_view(),name="artist_delete"),  
]
