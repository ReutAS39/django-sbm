from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    photo = models.ImageField(upload_to="person/%Y/%m/%d/", blank=True, verbose_name='Фото')
    # career = models.ManyToManyField(#, through='FilmActor')
    height = models.FloatField(blank=True, null=True, verbose_name='Рост')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    birthplace = models.CharField(max_length=255, blank=True, null=True, verbose_name='Место рождения')
    genres = models.ManyToManyField(Genre, through='PersonGenre', blank=True, verbose_name='Жанры')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person', args=[str(self.pk)])


class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')
    orig_title = models.CharField(max_length=255, verbose_name='Оригинальное название')
    age_rate = models.CharField(max_length=10, verbose_name='Возрастной рейтинг')
    year = models.IntegerField(verbose_name='Год производства')
    country = models.CharField(max_length=255, verbose_name='Страна')
    genre = models.ManyToManyField(Genre, through='FilmGenre', verbose_name='Жанр')
    tagline = models.CharField(max_length=255, verbose_name='Слоган')
    actor = models.ManyToManyField(Person, blank=True, through='FilmActor', related_name='film_actor', verbose_name='Актёр')
    director = models.ManyToManyField(Person, blank=True, through='FilmDirector', related_name='film_director', verbose_name='Режиссёр')
    writer = models.ManyToManyField(Person, blank=True, through='FilmWriter', related_name='film_writer', verbose_name='Сценарий')
    producer = models.ManyToManyField(Person, blank=True, through='FilmProducer', related_name='film_producer', verbose_name='Продюсер')
    operator = models.ManyToManyField(Person, blank=True, through='FilmOperator', related_name='film_operator', verbose_name='Оператор')
    composer = models.ManyToManyField(Person, blank=True, through='FilmComposer', related_name='film_composer', verbose_name='Композитор')
    budget = models.IntegerField(verbose_name='Бюджет')
    description = models.TextField(verbose_name='Обзор')
    poster = models.ImageField(upload_to="film/poster/%Y/%m/%d/", verbose_name='Постер')
    frame = models.ImageField(upload_to="film/frame/%Y/%m/%d/", verbose_name='Изображения')

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
