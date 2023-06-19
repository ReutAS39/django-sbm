from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Film(models.Model):
    title = models.CharField(max_length=255)
    orig_title = models.CharField(max_length=255)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, through='FilmGenre')
    tagline = models.CharField(max_length=255)
    actor = models.ManyToManyField(Actor, through='FilmActor')
    description = models.TextField()

    def __str__(self):
        return self.title

class FilmGenre(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)