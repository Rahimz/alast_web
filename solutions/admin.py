from django.contrib import admin

from .models import Solution, SolutionCategory, Award

# admin.site.register(Solution)
admin.site.register(SolutionCategory)

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'client']
    search_fields = ['title', 'client__name','description', 'product_model', 'designer', 'manufacturing_methods', ]
    prepopulated_fields = {"slug": ["title"]}


@admin.register(Award)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year',]
    