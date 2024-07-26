from django.contrib import admin

from .models import Image, Gallery


admin.site.register(Gallery)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'solution', 'gallery', 'zone',]