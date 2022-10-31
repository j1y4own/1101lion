# Generated by Django 4.0.6 on 2022-10-28 07:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cashbookapp', '0004_alter_cashbook_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashbook',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
