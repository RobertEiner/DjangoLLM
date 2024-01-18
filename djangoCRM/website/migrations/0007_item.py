# Generated by Django 5.0 on 2023-12-29 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_delete_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=50, verbose_name='Category')),
                ('price', models.CharField(max_length=7, verbose_name='Price')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]