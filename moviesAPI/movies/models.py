from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=500)
    pagelink = models.URLField(max_length=1000)
    sitename = models.CharField(max_length=500)
    image = models.URLField(blank=True, null=True)  # Assuming it's a URL, or use ImageField if storing images

    def __str__(self):
        return self.title