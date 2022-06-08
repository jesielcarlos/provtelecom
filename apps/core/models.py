from django.db import models
from apps.profileUser.models import ProfileUser


class Alerts(models.Model):
    profile = models.ForeignKey(ProfileUser, verbose_name="profile", on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=300, verbose_name='Conteúdo')
    title = models.CharField(max_length=100, verbose_name='Título')
    active = models.BooleanField(verbose_name="Active", default=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)

    def __str__(self):
        return self.title
