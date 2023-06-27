# Generated by Django 4.2.2 on 2023-06-27 12:09

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
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0.0)),
                ('orig_title', models.CharField(max_length=255)),
                ('age_rate', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('budget', models.IntegerField()),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='film/poster/%Y/%m/%d/')),
                ('frame', models.ImageField(upload_to='film/frame/%Y/%m/%d/')),
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
                ('name', models.CharField(max_length=255, unique=True)),
                ('photo', models.ImageField(upload_to='person/%Y/%m/%d/')),
                ('height', models.FloatField(blank=True, null=True)),
                ('date_of_birth', models.DateField()),
                ('birthplace', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
                ('rating', models.IntegerField(default=0)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_film', to='movies.film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_actor', to='movies.person')),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='genres',
            field=models.ManyToManyField(through='movies.PersonGenre', to='movies.genre'),
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
            field=models.ManyToManyField(related_name='film_actor', through='movies.FilmActor', to='movies.person'),
        ),
        migrations.AddField(
            model_name='film',
            name='composer',
            field=models.ManyToManyField(related_name='film_composer', through='movies.FilmComposer', to='movies.person'),
        ),
        migrations.AddField(
            model_name='film',
            name='director',
            field=models.ManyToManyField(related_name='film_director', through='movies.FilmDirector', to='movies.person'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(through='movies.FilmGenre', to='movies.genre'),
        ),
        migrations.AddField(
            model_name='film',
            name='operator',
            field=models.ManyToManyField(related_name='film_operator', through='movies.FilmOperator', to='movies.person'),
        ),
        migrations.AddField(
            model_name='film',
            name='producer',
            field=models.ManyToManyField(related_name='film_producer', through='movies.FilmProducer', to='movies.person'),
        ),
        migrations.AddField(
            model_name='film',
            name='writer',
            field=models.ManyToManyField(related_name='film_writer', through='movies.FilmWriter', to='movies.person'),
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
