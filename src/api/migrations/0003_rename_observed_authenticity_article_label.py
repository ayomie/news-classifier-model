# Generated by Django 4.0 on 2021-12-23 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_article_text_alter_feedback_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='observed_authenticity',
            new_name='label',
        ),
    ]
