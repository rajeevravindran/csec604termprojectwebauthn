# Generated by Django 3.1.3 on 2020-11-22 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangowebauthn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webauthnprofile',
            name='webauthn_ukey',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
