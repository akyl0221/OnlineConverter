from django.contrib import admin
from .models import Download


class DownloadAdmin(admin.ModelAdmin):
    list_display = ('url', 'date_load')


admin.site.register(Download, DownloadAdmin)