from django.conf import settings
from django.db import models


class ProfileUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='user', on_delete=models.DO_NOTHING)
    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    theme_dark = models.BooleanField(verbose_name="Theme Dark", default=True)

    def __str__(self):
        return self.user.username
