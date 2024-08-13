# Generated by Django 4.2.13 on 2024-08-12 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0002_alter_ad_category_alter_ad_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'Отклик', 'verbose_name_plural': 'Отклики'},
        ),
        migrations.AddField(
            model_name='ad',
            name='upload',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.CharField(choices=[('TA', 'Танки'), ('HI', 'Хилы'), ('DD', 'ДД'), ('DE', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('BS', 'Кузнецы'), ('TA', 'Кожевники'), ('PM', 'Зельевары'), ('SM', 'Мастера заклинаний')], default='TA', max_length=2, verbose_name='Категория'),
        ),
    ]