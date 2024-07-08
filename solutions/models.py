from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from tools.models import TimeStampedModel
from tools.make_thumbnail import make_thumbnail

class SolutionCategory(TimeStampedModel):
    parent = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        verbose_name=_("Parent"),
        null=True, 
        blank=True, 
    )
    name = models.CharField(
        _("Name"),
        max_length=250,
        unique=True,
    )
    slug = models.SlugField(
        _("Slug"),
        allow_unicode=True        
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        return super().save(*args, **kwargs)
    

class Solution(TimeStampedModel):
    title = models.CharField(
        _("Title"),        
        max_length=255,
        unique=True
    )
    slug = models.SlugField(
        _("Slug"),
        allow_unicode=True
    )
    category = models.ForeignKey(
        SolutionCategory, 
        on_delete=models.SET_NULL,
        verbose_name=_("Category"),
        related_name='solutions',
        null=True, 
        blank=True, 
    )
    description = models.TextField(
        _("Description"),
    )
    cover_image = models.ImageField(
        _("Cover image"),
        upload_to='solutions/cover_images/'
    )
    thumbnail = models.ImageField(
        upload_to='solutions/thumbnails/',
        null=True,
        blank=True
    )
    # client = mdoels.CharField(null=True, blank=True)
    # client_logo = models.ImageField(null=True, blank=True)
    

    def save(self, *args, **kwargs):
        self.thumbnail = make_thumbnail(self.cover_image)
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)