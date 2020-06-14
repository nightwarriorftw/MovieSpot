from django.contrib import admin

from .models import MovieSpotModel

class MovieSpotAdmin(admin.ModelAdmin):
    class Meta:
        models = MovieSpotModel
        fields = '__all__'

admin.site.register(MovieSpotModel, MovieSpotAdmin)
