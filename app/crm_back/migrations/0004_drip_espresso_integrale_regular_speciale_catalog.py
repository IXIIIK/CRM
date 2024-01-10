# Generated by Django 4.2.3 on 2024-01-09 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm_back', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='Введите вес: ')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramm'), ('GR', 'Grams')], help_text='Введите еденицу измерения: ', max_length=2)),
                ('price', models.IntegerField(help_text='Введите сумму')),
                ('name', models.CharField(help_text='Введите название: ', max_length=64)),
                ('description', models.TextField(help_text='Введите описапние: ', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Espresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='Введите вес: ')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramm'), ('GR', 'Grams')], help_text='Введите еденицу измерения: ', max_length=2)),
                ('price', models.IntegerField(help_text='Введите сумму')),
                ('name', models.CharField(help_text='Введите название: ', max_length=64)),
                ('description', models.TextField(help_text='Введите описапние: ', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Integrale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='Введите вес: ')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramm'), ('GR', 'Grams')], help_text='Введите еденицу измерения: ', max_length=2)),
                ('price', models.IntegerField(help_text='Введите сумму')),
                ('name', models.CharField(help_text='Введите название: ', max_length=64)),
                ('description', models.TextField(help_text='Введите описапние: ', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Regular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='Введите вес: ')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramm'), ('GR', 'Grams')], help_text='Введите еденицу измерения: ', max_length=2)),
                ('name', models.CharField(help_text='Введите название: ', max_length=64)),
                ('price', models.IntegerField(help_text='Введите сумму')),
                ('description', models.TextField(help_text='Введите описапние: ', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Speciale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField(help_text='Введите вес: ')),
                ('unit', models.CharField(choices=[('KG', 'Kilogramm'), ('GR', 'Grams')], help_text='Введите еденицу измерения: ', max_length=2)),
                ('price', models.IntegerField(help_text='Введите сумму')),
                ('name', models.CharField(help_text='Введите название: ', max_length=64)),
                ('description', models.TextField(help_text='Введите описапние: ', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drip', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm_back.drip')),
                ('espresso', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm_back.espresso')),
                ('integrale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm_back.integrale')),
                ('regular', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm_back.regular')),
                ('speciale', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crm_back.speciale')),
            ],
        ),
    ]
