# Generated by Django 2.2.17 on 2021-03-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kydolex_app', '0003_auto_20210303_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='kydolex_list_3d',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_3d',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_blog',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_blog',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_graphic',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_graphic',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_icon',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_icon',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_image',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_image',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_photograth',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_photograth',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_uiux',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_uiux',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='kydolex_list_video',
            name='content',
            field=models.TextField(max_length=200, null=True, verbose_name='説明'),
        ),
        migrations.AddField(
            model_name='kydolex_list_video',
            name='content_url',
            field=models.TextField(max_length=200, null=True, verbose_name='URL'),
        ),
    ]
