from django.db import models
from apps.profileUser.models import ProfileUser
from django.utils.translation import gettext as _


class Called(models.Model):

    OPEN = 0
    CLOSED = 1
    IN_PROGRESS = 2

    SITUATIONS = (
        (OPEN, _('Open')),
        (CLOSED, _('Closed')),
        (IN_PROGRESS, _('In Progress')),
    )

    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    profile = models.ForeignKey(ProfileUser, verbose_name="profile", on_delete=models.DO_NOTHING)
    title = models.CharField(verbose_name="Title", max_length=200)
    description = models.CharField(verbose_name="Description", max_length=500)
    situation = models.IntegerField(verbose_name="Situation", choices=SITUATIONS, default=OPEN)

    def __str__(self):
        return self.title
