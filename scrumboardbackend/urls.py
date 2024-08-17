from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('user_auth.urls')),  # Authentifizierung und Registrierung
    path('todos/', include('todolist.urls')),  # To-Do-Listen-Management
    path('users/', include('users.urls')),  # Benutzerverwaltung
]
