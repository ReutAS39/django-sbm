from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Имя')
    orig_name = models.CharField(max_length=255, unique=True, blank=True, verbose_name='Оригинальное имя')
    photo = models.ImageField(upload_to="person/%Y/%m/%d/", blank=True, verbose_name='Фото')
    # career = models.ManyToManyField(#, through='FilmActor')
    height = models.FloatField(blank=True, null=True, verbose_name='Рост')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    birthplace = models.CharField(max_length=255, blank=True, null=True, verbose_name='Место рождения')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('person_detail', args=[str(self.pk)])


class Film(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    rating = models.FloatField(default=0.0, verbose_name='Рейтинг')
    orig_title = models.CharField(max_length=100, blank=True, verbose_name='Оригинальное название')
    age_rate = models.CharField(max_length=10, blank=True, verbose_name='Возрастной рейтинг')
    year = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Год производства')
    country = models.CharField(max_length=50, blank=True, verbose_name='Страна')
    genre = models.ManyToManyField(Genre, through='FilmGenre', related_name='film_genre', verbose_name='Жанр', blank=True)
    tagline = models.CharField(max_length=100, blank=True, verbose_name='Слоган')
    actor = models.ManyToManyField(Person, blank=True, through='FilmActor', related_name='film_actor', verbose_name='Актёр')
    director = models.ManyToManyField(Person, blank=True, through='FilmDirector', related_name='film_director', verbose_name='Режиссёр')
    writer = models.ManyToManyField(Person, blank=True, through='FilmWriter', related_name='film_writer', verbose_name='Сценарий')
    producer = models.ManyToManyField(Person, blank=True, through='FilmProducer', related_name='film_producer', verbose_name='Продюсер')
    operator = models.ManyToManyField(Person, blank=True, through='FilmOperator', related_name='film_operator', verbose_name='Оператор')
    composer = models.ManyToManyField(Person, blank=True, through='FilmComposer', related_name='film_composer', verbose_name='Композитор')
    budget = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Бюджет')
    gross_worldwide = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Сборы в мире', default=0)
    world_premiere = models.DateField(null=True,blank=True, verbose_name='Премьера в мире')
    runtime = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Хронометраж')
    description = models.TextField(verbose_name='Обзор')
    poster = models.ImageField(upload_to="film/poster/%Y/%m/%d/", null=True, verbose_name='Постер')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.pk)])


class FilmFrame(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    frame = models.ImageField(upload_to="film/frame/%Y/%m/%d/", verbose_name='Изображения')


class FilmGenre(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='genre_film')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class FilmActor(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='actor_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return 'Актёр'


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

    def __str__(self):
        return 'Оператор'

class FilmComposer(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='composer_film')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return 'Композитор'

class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews_film')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments_review')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
