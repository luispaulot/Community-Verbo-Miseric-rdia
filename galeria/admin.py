from django.contrib import admin

from .models import Album, Foto


class FotoInline(admin.TabularInline):
    model = Foto
    extra = 5


class AlbumAdmin(admin.ModelAdmin):
    inlines = [FotoInline]


admin.site.register(Album, AlbumAdmin)
