# Generated by Django 3.2.21 on 2023-10-30 15:21

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20231023_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_quill.fields.QuillField(default='body'),
        ),
    ]