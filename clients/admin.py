from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    prepopulated_fields = {"slug": ["name"]}
    search_fields = ['name']


