import binascii
import datetime
import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    USER_CATEGORY_CHOICES = (('local', 'Local'), ('ldap', 'LDAP'))
    category = models.CharField(
        _('user category'), choices=USER_CATEGORY_CHOICES, max_length=20, default='local', null=False)

    def is_today_join(self):
        return self.date_joined.date() == datetime.date.today()


def _default_expire_time():
    return timezone.now() + Token.TOKEN_EXPIRE


class Token(models.Model):
    TOKEN_LENGTH = 32
    TOKEN_EXPIRE = datetime.timedelta(minutes=10)

    user = models.ForeignKey(
        'User', verbose_name=_("User"), related_name='tokens', on_delete=models.CASCADE, null=True, blank=False
    )
    created = models.DateTimeField(_('create time'), auto_now_add=True)
    expired = models.DateTimeField(_('token expire time'), default=_default_expire_time)
    token = models.TextField(_('token'), blank=True)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(int(self.TOKEN_LENGTH / 2))).decode()
