from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from tools.models import TimeStampedModel

class User(AbstractUser, PermissionsMixin):
    pass


class TeamMember(TimeStampedModel):
    user = models.OneToOneField(
        User,
        related_name='team_member',
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        _("Avatar"),
        upload_to='multimedias/team_members/',
    )
    role = models.CharField(
        _("Role"),
        max_length=150,
        null=True,
        blank=True,
    )
    bio = models.TextField(
        _("Biography"),
        blank=True,
    )
    rank = models.IntegerField(
        _("Rank"),
        default=1
    )
    linkedin = models.URLField(
        _("Linkedin"),
        null=True,
        blank=True
    )
    instagram = models.URLField(
        _("Instagram"),
        null=True,
        blank=True
    )
    behance = models.URLField(
        _("Behance"),
        null=True,
        blank=True
    )
    dribbble = models.URLField(
        _("Dribbble"),
        null=True,
        blank=True
    )
    tiwtter = models.URLField(
        _("Tiwtter"),
        null=True,
        blank=True
    )
    Link = models.URLField(
        _("Link"),
        null=True,
        blank=True
    )


    def __str__(self):
        return self.user.username
    