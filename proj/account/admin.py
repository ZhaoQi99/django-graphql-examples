from django.contrib import admin
from account.models import User,Token

admin.site.register(User)
admin.site.register(Token)