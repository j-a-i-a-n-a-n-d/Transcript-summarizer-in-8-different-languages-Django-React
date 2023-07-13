from django.contrib import admin

# Register your models here.
from .models import YoutubeModel


class YtAdmin(admin.ModelAdmin):
    list_display = ('url', 'summary')


admin.site.register(YoutubeModel, YtAdmin)
