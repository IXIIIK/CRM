# Generated by Django 4.2.3 on 2024-01-27 01:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_back', '0010_order_delete_opt_order_alter_catalog_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(blank=True, help_text='Введите имя', max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(blank=True, help_text='Введите фамилию', max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_catalog',
            field=models.ForeignKey(blank=True, help_text='Выберете товар', on_delete=django.db.models.deletion.CASCADE, to='crm_back.catalog', verbose_name='Товар'),
        ),
    ]