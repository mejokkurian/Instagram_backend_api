# Generated by Django 3.2.7 on 2022-01-03 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_postcomments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomments',
            old_name='Post_id',
            new_name='post_id',
        ),
    ]
