# Generated by Django 4.0 on 2021-12-23 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_article_predicted_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='predicted_label',
            field=models.BooleanField(default=None, null=True),
        ),
    ]