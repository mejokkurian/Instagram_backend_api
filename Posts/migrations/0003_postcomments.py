# Generated by Django 3.2.7 on 2022-01-03 04:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Posts', '0002_postlikes'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('Post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Posts.posts')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
