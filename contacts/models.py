from django.db import models

from users.models import CustomUser

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contacts', default=1)  # Standardmäßig den Benutzer mit ID 1 verwenden

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    