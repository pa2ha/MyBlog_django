# Generated by Django 3.2.16 on 2023-05-25 12:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_rename_commentmodel_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='CommentModel',
        ),
    ]
