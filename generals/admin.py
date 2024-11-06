from django.contrib import admin

from .models import Contact, LogoMotion


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'created']
    search_fields = ['name', 'email', 'message']

@admin.register(LogoMotion)
class LogoMotionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'file', 'active']
    
