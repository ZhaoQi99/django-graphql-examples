# Generated by Django 4.0.5 on 2022-06-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('local', 'Local'), ('ldap', 'LDAP')], default='local', max_length=20, verbose_name='user category'),
        ),
    ]
