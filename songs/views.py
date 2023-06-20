from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from albums.models import Album
from .models import Song
from .serializers import SongSerializer


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        album_pk = self.kwargs["pk"]
        return Song.objects.filter(album_id=album_pk)

    def perform_create(self, serializer):
        album_pk = self.kwargs["pk"]
        album = get_object_or_404(Album, pk=album_pk)
        return serializer.save(album=album)
