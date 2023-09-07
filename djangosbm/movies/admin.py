from django.contrib import admin
from django.utils.safestring import mark_safe

from movies.models import Film, Genre, Person, FilmFrame, Review, FilmGenre, FilmActor, FilmDirector, FilmWriter, \
    FilmProducer, FilmOperator, FilmComposer, RatingStar, Rating


class ActorInlines(admin.StackedInline):
    model = FilmActor
    extra = 1

class DirectorInlines(admin.StackedInline):
    model = FilmDirector
    extra = 1

class WriterInlines(admin.StackedInline):
    model = FilmWriter
    extra = 1

class ProducerInlines(admin.StackedInline):
    model = FilmProducer
    extra = 1

class OperatorInlines(admin.StackedInline):
    model = FilmOperator
    extra = 1

class ComposerInlines(admin.StackedInline):
    model = FilmComposer
    extra = 1

class GenreInlines(admin.StackedInline):
    model = FilmGenre
    extra = 1

class FilmFrameInlines(admin.StackedInline):
    model = FilmFrame
    extra = 1
    readonly_fields = ('get_frame',)

    def get_frame(self, obj):
        return mark_safe(f'<img src={obj.frame.url} width="100" height="110"')

    get_frame.short_description = "Изображение"

class ReviewInlines(admin.StackedInline):
    model = Review
    extra = 1
    readonly_fields = ('user', )

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    list_filter = ('genre', 'year', )
    search_fields = ('title', )
    readonly_fields = ('get_poster',)
    inlines = [GenreInlines, FilmFrameInlines, ActorInlines, DirectorInlines, WriterInlines, ProducerInlines, OperatorInlines, ComposerInlines, ReviewInlines]
    save_on_top = True  # перенос кнопки сохранения наверх
    save_as = True
    # fields = ('film_actor',)
    # fieldsets = (
    #     (None, {
    #         "fields": (('actor',),)
    #     }),
    # )
    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_poster.short_description = "Изображение"

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'orig_name', 'get_photo')
    list_display_links = ('name',)
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50" height="60"')

    get_photo.short_description = "Изображение"

class FilmFrameAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'get_frame')
    list_display_links = ('film',)
    readonly_fields = ('get_frame',)

    def get_frame(self, obj):
        return mark_safe(f'<img src={obj.frame.url} width="50" height="60"')

    get_frame.short_description = "Изображение"

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'text',)
    readonly_fields = ('user', )


class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('film', 'star', 'ip')


# admin.site.register(Film, FilmAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(FilmFrame, FilmFrameAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(RatingStar, RatingStarAdmin)
admin.site.register(Rating, RatingAdmin)