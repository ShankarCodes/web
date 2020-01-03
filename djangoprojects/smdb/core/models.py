from django.db import models
import uuid
# Create your models here.
class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    RATINGS = (
        (0, 'NR - Not Rated'),
        (1, 'G  - General Audience'),
        (2, 'PG - Parental Guidance Suggested'),
        (3, 'R  - Restricted'),
    )
    title = models.CharField(max_length=150)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS,default=0)
    runtime = models.PositiveIntegerField()
    website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.title}({self.year})"
        