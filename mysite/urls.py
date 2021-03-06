from django.contrib import admin
from django.urls import path, include  # <-- Make sure you have both of these imports.

urlpatterns = [
    path('polling/', include('polling.urls')),  # <-- Add this
    path('admin/', admin.site.urls),
    path('', include('blogging.urls')),
    path('accounts/', include('allauth.urls')),
]