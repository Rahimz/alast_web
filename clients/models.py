from django.db import models
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel


class Client(TimeStampedModel):
    name = models.CharField(
        _("Name"),
        max_length=250,
    )
    slug = models.SlugField(
        _("Slug"),
        allow_unicode=True,
    )
    logo = models.ImageField(
        _("Client logo"),
        upload_to='clients/logos/'        
    )
    
    def __str__(self):
        return self.name
    
