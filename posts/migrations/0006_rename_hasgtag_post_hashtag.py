# Generated by Django 4.1.3 on 2022-11-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_remove_post_hashtag_post_hasgtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='hasgtag',
            new_name='hashtag',
        ),
    ]
