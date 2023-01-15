# Generated by Django 4.1.4 on 2023-01-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('-year',)},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ('-year',)},
        ),
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='', upload_to='service_img/'),
            preserve_default=False,
        ),
    ]
