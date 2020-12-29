# Generated by Django 3.1.4 on 2020-12-29 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AddField(
            model_name='article',
            name='number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='para',
            field=models.TextField(default='para'),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]