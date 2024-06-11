# Generated by Django 5.0.3 on 2024-05-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vg_projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfildev',
            name='archivo_proyecto',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='perfildev',
            name='descripcion_proyecto',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='perfildev',
            name='imagen_perfil',
            field=models.ImageField(blank=True, upload_to='imagen'),
        ),
        migrations.AddField(
            model_name='perfildev',
            name='sobremi',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='correo_perfil',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='facebook_perfil',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='github_perfil',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='instagram_perfil',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='nombre_perfil',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='twitch_perfil',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='perfildev',
            name='youtube_perfil',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
