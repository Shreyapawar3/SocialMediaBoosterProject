from django.db import models
from django.utils import timezone

class Item(models.Model):
    """
    Simple Item model used by the project (title, content, created_at).
    """
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title