import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_CATEGORY_CHOICES = (('local', 'Local'), ('ldap', 'LDAP'))
    category = models.CharField(_('user category'), choices=USER_CATEGORY_CHOICES, max_length=20, default='local', null=False)

    def is_today_join(self):
        return self.date_joined.date() == datetime.date.today()