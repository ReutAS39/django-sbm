# Generated by Django 4.2.2 on 2023-08-17 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('rating', models.FloatField(default=0.0, verbose_name='Рейтинг')),
                ('orig_title', models.CharField(max_length=100, verbose_name='Оригинальное название')),
                ('age_rate', models.CharField(max_length=10, verbose_name='Возрастной рейтинг')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Год производства')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('tagline', models.CharField(max_length=100, verbose_name='Слоган')),
                ('budget', models.PositiveSmallIntegerField(verbose_name='Бюджет')),
                ('gross_worldwide', models.PositiveSmallIntegerField(default=0, verbose_name='Сборы в мире')),
                ('world_premiere', models.DateField(verbose_name='Премьера в мире')),
                ('runtime', models.PositiveSmallIntegerField(verbose_name='Хронометраж')),
                ('description', models.TextField(verbose_name='Обзор')),
                ('poster', models.ImageField(upload_to='film/poster/%Y/%m/%d/', verbose_name='Постер')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Имя')),
                ('orig_name', models.CharField(max_length=255, unique=True, verbose_name='Оригинальное имя')),
                ('photo', models.ImageField(blank=True, upload_to='person/%Y/%m/%d/', verbose_name='Фото')),
                ('height', models.FloatField(blank=True, null=True, verbose_name='Рост')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('birthplace', models.CharField(blank=True, max_length=255, null=True, verbose_name='Место рождения')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=255)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_film', to='movies.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FilmWriter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer_film', to='movies.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='FilmProducer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producer_film', to='movies.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='FilmOperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operator_film', to='movies.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='FilmGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_film', to='movies.film')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='FilmFrame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.ImageField(upload_to='film/frame/%Y/%m/%d/', verbose_name='Изображения')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.film')),
            ],
        ),
        migrations.CreateModel(
            name='FilmDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='director_film', to='movies.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='FilmComposer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='composer_film', to='movies.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor_film', to='movies.film')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='actor',
            field=models.ManyToManyField(blank=True, related_name='film_actor', through='movies.FilmActor', to='movies.person', verbose_name='Актёр'),
        ),
        migrations.AddField(
            model_name='film',
            name='composer',
            field=models.ManyToManyField(blank=True, related_name='film_composer', through='movies.FilmComposer', to='movies.person', verbose_name='Композитор'),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(blank=True, related_name='film_director', through='movies.FilmDirector', to='movies.person', verbose_name='Режиссёр'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(through='movies.FilmGenre', to='movies.genre', verbose_name='Жанр'),
        ),
        migrations.AddField(
            model_name='film',
            name='operator',
            field=models.ManyToManyField(blank=True, related_name='film_operator', through='movies.FilmOperator', to='movies.person', verbose_name='Оператор'),
        ),
        migrations.AddField(
            model_name='film',
            name='producer',
            field=models.ManyToManyField(blank=True, related_name='film_producer', through='movies.FilmProducer', to='movies.person', verbose_name='Продюсер'),
        ),
        migrations.AddField(
            model_name='film',
            name='writer',
            field=models.ManyToManyField(blank=True, related_name='film_writer', through='movies.FilmWriter', to='movies.person', verbose_name='Сценарий'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_review', to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
