from django.db import models
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel


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
