from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.year})' # f-string: to help format view on admin site