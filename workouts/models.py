from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    sets_reps = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    images = models.JSONField()  # Store a list of image URLs

    def __str__(self):
        return self.title
