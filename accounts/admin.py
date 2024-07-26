from django.contrib import admin

from .models import User, TeamMember


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'last_name']
    

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'rank']
    list_editable = ['rank']