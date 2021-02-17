# Generated by Django 3.0 on 2021-02-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20210212_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'В обработке'), (1, 'Отправлен'), (2, 'Получен')], default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
