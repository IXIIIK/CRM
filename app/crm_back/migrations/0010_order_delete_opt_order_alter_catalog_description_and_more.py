# Generated by Django 4.2.3 on 2024-01-27 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_back', '0009_catalog_opt_order_delete_new_unit_delete_test_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(blank=True, choices=[('NEW', 'Новый заказ'), ('WAIT_PAID', 'Ждут отплаты'), ('STARTED', 'В работе'), ('READY', 'Отгружен')], help_text='Выберете статус:', max_length=10, verbose_name='Статус')),
                ('first_name', models.CharField(help_text='Введите имя', max_length=64, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=64, verbose_name='Фамилия')),
            ],
        ),
        migrations.DeleteModel(
            name='Opt_order',
        ),
        migrations.AlterField(
            model_name='catalog',
            name='description',
            field=models.TextField(help_text='Введите описапние: ', max_length=256, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='mass',
            field=models.CharField(choices=[('Kilogramms', 'Кг'), ('Gramms', 'Гр')], help_text='Выберете массу: ', max_length=64, verbose_name='Масса'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name',
            field=models.CharField(help_text='Введите название: ', max_length=64, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='price',
            field=models.IntegerField(help_text='Введите сумму: ', verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='unit',
            field=models.CharField(choices=[('RG', 'Regular'), ('SC', 'Speciale'), ('IG', 'Integrale'), ('ES', 'Espresso'), ('DR', 'Drip')], help_text='Выберете сорт: ', max_length=9, verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='weight',
            field=models.IntegerField(help_text='Введите вес: ', verbose_name='Вес'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_catalog',
            field=models.ForeignKey(help_text='Выберете товар', on_delete=django.db.models.deletion.CASCADE, to='crm_back.catalog', verbose_name='Товар'),
        ),
    ]
