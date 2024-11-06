from django.contrib import admin

from .models import Solution, SolutionCategory, Award
from multimedias.models import Image

class ImageGalleryInline(admin.StackedInline):
    model = Image
    raw_id_fields = ('solution',)
    exclude = ['zone', 'gallery', 'thumbnail']
    max_num = 2


# admin.site.register(Solution)
@admin.register(SolutionCategory)
class SolutionCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    search_fields = ['name']

@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'client']
    search_fields = ['title', 'client', 'client__name','description', 'product_model', 'designer', 'manufacturing_methods', ]
    prepopulated_fields = {"slug": ["title"]}
    
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'category', 'client')
        }),
        ('Product Information', {
            'fields': ('product_model', 'design_date', 'designer', 'manufacturing_methods', 'description', 'tags')
        }),
        ('Images', {
            'fields': ('cover_image', 'thumbnail')
        }),
        ('Status', {
            'fields': ('active',)
        }),       
    )
    inlines = [ImageGalleryInline]
    autocomplete_fields = ['client', 'category']


@admin.register(Award)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'year',]
    