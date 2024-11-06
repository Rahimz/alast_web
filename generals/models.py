from django.db import models
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel, ActiveManager


class Contact(TimeStampedModel):
    name = models.CharField(
        _("Name"),
        max_length=150
    )
    email = models.EmailField(
        _("Email")
    )
    message = models.TextField(
        _("Message"),
    )

    def __str__(self):
        return self.name
    
    class Meta:        
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')
        ordering = ('-id',)


class LogoMotion(TimeStampedModel):
    name = models.CharField(
        _("Name"),
        max_length=150,
    )
    file = models.FileField(
        _("File"),
        upload_to='generals/logo/',
        help_text=_("Just upload video files"),
    )
    active = models.BooleanField(
        default=True
    )
    objects = models.Manager()
    actives = ActiveManager()