from django.db import models
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel
from tools.make_thumbnail import make_thumbnail
from solutions.models import Solution


class Image(TimeStampedModel):
    solution = models.ForeignKey(
        Solution,
        verbose_name=_("Solution"),
        related_name='images',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    title = models.CharField(
        _("Title"),
        max_length=150,
        null=True,
        blank=True
    )
    file = models.ImageField(
        _("File"),
        upload_to='multimedias/images/',
    )
    image_alt = models.CharField(
        _("Image alt"),
        max_length=150,
        null=True,
        blank=True,
    )
    thumbnail = models.ImageField(
        _("Thumbnail"),
        upload_to='multimedias/images/thumbnails/',
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        self.thumbnail = make_thumbnail(self.file.file)
        return super().save(*args, **kwargs)
