from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # career = models.ManyToManyField(#, through='FilmActor')
    height = models.FloatField()
    date_of_birth = models.DateField()
    birthplace = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, through='ActorGenre')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor', args=[str(self.pk)])


class Film(models.Model):
    title = models.CharField(max_length=255)
    orig_title = models.CharField(max_length=255)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, through='FilmGenre')
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to="media/%Y/%m/%d/")
    actor = models.ManyToManyField(Actor, through='FilmActor')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film', args=[str(self.pk)])

class FilmGenre(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='genre_film')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class ActorGenre(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='genre_actor')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='actor_film')
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)