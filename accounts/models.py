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
        upload_to='mutlimedias/team_members/',
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

    def __str__(self):
        return self.user.username
    