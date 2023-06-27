from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to="person/%Y/%m/%d/")
    # career = models.ManyToManyField(#, through='FilmActor')
    height = models.FloatField(blank=True, null=True)
    date_of_birth = models.DateField()
    birthplace = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, through='PersonGenre')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person', args=[str(self.pk)])


class Film(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField(default=0.0)
    orig_title = models.CharField(max_length=255)
    age_rate = models.CharField(max_length=10)
    year = models.IntegerField()
    country = models.CharField(max_length=255)
    genre = models.ManyToManyField(Genre, through='FilmGenre')
    tagline = models.CharField(max_length=255)
    actor = models.ManyToManyField(Person, through='FilmActor', related_name='film_actor')
    director = models.ManyToManyField(Person, through='FilmDirector', related_name='film_director')
    writer = models.ManyToManyField(Person, through='FilmWriter', related_name='film_writer')
    producer = models.ManyToManyField(Person, through='FilmProducer', related_name='film_producer')
    operator = models.ManyToManyField(Person, through='FilmOperator', related_name='film_operator')
    composer = models.ManyToManyField(Person, through='FilmComposer', related_name='film_composer')
    budget = models.IntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to="film/poster/%Y/%m/%d/")
    frame = models.ImageField(upload_to="film/frame/%Y/%m/%d/")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film', args=[str(self.pk)])


class FilmGenre(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='genre_film')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class PersonGenre(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='genre_actor')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='actor_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class FilmDirector(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='director_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class FilmWriter(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='writer_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class FilmProducer(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='producer_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class FilmOperator(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='operator_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class FilmComposer(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='composer_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews_film')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments_review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
