from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models.fields import DateTimeField

from whatsplaying.core.models import TimeStampedModel


class Movie(TimeStampedModel):
    directed_by = ArrayField(models.CharField(), blank=True)
    poster_url = models.CharField(blank=True)
    rating = models.CharField(max_length=10, blank=True)
    runtime = models.DurationField(blank=True)
    title = models.CharField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Venue(TimeStampedModel):
    name = models.CharField()
    address = models.CharField(blank=True)
    currently_showing = models.ManyToManyField(Movie, related_name="venues", blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Showtime(TimeStampedModel):
    movie = models.ForeignKey(Movie, related_name="showtimes", on_delete=models.CASCADE)
    time = models.DateTimeField()
    venue = models.ForeignKey(Venue, related_name="showtimes", on_delete=models.CASCADE)

    class Meta:
        ordering = ["time"]

    def __str__(self):
        return f"{self.movie.title} at {self.venue.name} - {self.time.strftime('%Y-%m-%d %H:%M')}"
