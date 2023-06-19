from django.contrib import admin

from movies.models import Film, Genre, Actor


class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    # list_filter = ('position', 'time_in', 'category__name')  # добавляем примитивные фильтры в нашу админку
    # search_fields = ('article', 'text')  # тут всё очень похоже на фильтры из запросов в базу

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    # list_filter = ('position', 'time_in', 'category__name')  # добавляем примитивные фильтры в нашу админку
    # search_fields = ('article', 'text')  # тут всё очень похоже на фильтры из запросов в базу

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
# list_filter = ('position', 'time_in', 'category__name')  # добавляем примитивные фильтры в нашу админку
# search_fields = ('article', 'text')  # тут всё очень похоже на фильтры из запросов в базу


admin.site.register(Film, FilmAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor, ActorAdmin)

