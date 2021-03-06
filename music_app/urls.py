
from django.contrib import admin
from django.urls import path
# from music_app.views import get_music, music_detail, music_create, MusicListView
from music_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', MusicListView.as_view()),
    path('music-create/', MusicCreateView.as_view()),
    path('music-update/<int:pk>/', MusicUpdateView.as_view()),
    path('music-detail/<int:pk>/', MusicDetailView.as_view()),
    path('music-delete/<int:pk>/', MusicDeleteView.as_view()),

    # path('music/', get_music),
    # path('music/<int:id>/', music_detail),
    # path('music-create/', music_create),


]
