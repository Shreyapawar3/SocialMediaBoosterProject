from django.db import models
from django.utils import timezone

class Report(models.Model):
    """
    Simple Report model storing metadata and report payload (JSON) for reporting/visualization.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    generated_by = models.CharField(max_length=150, blank=True)
    data = models.JSONField(blank=True, null=True)  # Postgres JSON storage for metrics/results
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'

    def __str__(self):
        return f"{self.title} ({self.created_at:%Y-%m-%d %H:%M})"