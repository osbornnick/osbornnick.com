# Generated by Django 2.2.5 on 2019-11-25 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='default', editable=False),
        ),
    ]
