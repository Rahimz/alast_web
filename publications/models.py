from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify

from tools.models import TimeStampedModel


class Publication(TimeStampedModel):
    title = models.CharField(
        _("Title"),
        max_length=250,
    )
    subtitle = models.CharField(
        _("Sub title"),
        max_length=250,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        allow_unicode=True,
        null=True,
        blank=True
    )
    authors = models.CharField(
        _("Authors"),
        max_length=350,
    )
    abstract = models.TextField(
        _("Abstract"),
        blank=True
    )
    pdf = models.FileField(
        _("PDF file"),
        upload_to='publications/pdf/',
        validators=[FileExtensionValidator(['pdf'])]
    )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)