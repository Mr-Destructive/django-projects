from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('world-atlas/', include('worldatlas.urls'), name='world-atlas-api'),
    path('dj-notes/', include('djnotes.urls'), name='dj-notes'),
    path('user/', include('user.urls'), name='user'),
]
