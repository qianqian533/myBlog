# Generated by Django 4.0 on 2022-01-06 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blogs', '0003_remove_blogpost_text_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='own',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]