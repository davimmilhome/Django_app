# Generated by Django 4.0.6 on 2022-07-08 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_post_altered_post_criate_post_publicadted_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publicated',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publicadted',
            new_name='publicated',
        ),
    ]
