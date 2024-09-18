from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

OWNER = get_user_model()

class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = "panding", "Panding",
        PROGRESS = "progres", "Progres",
        COMPLETED = "completed", "Completed",
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=100, choices=Status, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(OWNER, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]
        
    def __str__(self) -> str:
        return f"{self.title} --> {self.status}" 