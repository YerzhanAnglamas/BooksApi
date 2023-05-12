# Generated by Django 4.2.1 on 2023-05-11 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='blog.author'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=155),
        ),
    ]
