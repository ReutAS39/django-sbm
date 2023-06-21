# Generated by Django 4.2.2 on 2023-06-21 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('height', models.FloatField()),
                ('date_of_birth', models.DateField()),
                ('birthplace', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('orig_title', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('tagline', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('poster', models.ImageField(upload_to='media/%Y/%m/%d/')),
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
            name='FilmGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_film', to='movies.film')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor_film', to='movies.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='actor',
            field=models.ManyToManyField(through='movies.FilmActor', to='movies.actor'),
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(through='movies.FilmGenre', to='movies.genre'),
        ),
        migrations.CreateModel(
            name='ActorGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_actor', to='movies.actor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
        migrations.AddField(
            model_name='actor',
            name='genres',
            field=models.ManyToManyField(through='movies.ActorGenre', to='movies.genre'),
        ),
    ]
