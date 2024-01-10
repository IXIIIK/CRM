from django.db import models

# Create your models here.
#Const
MASS = [
        ('KG', 'Kilogramm'),
        ('GR', 'Grams')
    ]

#Document
class Provider(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)


class Payer(models.Model):
    pass


class Torg(models.Model):
    name = models.CharField(max_length=64)
    shipper = models.CharField(max_length=128)
    adress = models.CharField(max_length=128)
    requisites = models.CharField(max_length=128)
    phone = models.IntegerField()
    ocpd = models.IntegerField()
    provider = models.ManyToManyField(Provider)
    payer = models.ManyToManyField(Payer)
    data = models.DateField()
    pact = models.IntegerField()

    def __str__(self):
        return self.name


#Main catalog with coffee 
class Regular(models.Model):
    weight = models.IntegerField(help_text='Введите вес: ')
    unit = models.CharField(max_length=2,
                            choices=MASS,
                            help_text='Введите еденицу измерения: '
                            )
    name = models.CharField(max_length=64, help_text='Введите название: ')
    price = models.IntegerField(help_text='Введите сумму')
    description = models.TextField(max_length=256, help_text='Введите описапние: ')

    def __str__(self):
        return self.name

class Speciale(models.Model):
    weight = models.IntegerField(help_text='Введите вес: ')
    unit = models.CharField(max_length=2,
                            choices=MASS,
                            help_text='Введите еденицу измерения: '
                            )
    price = models.IntegerField(help_text='Введите сумму')
    name = models.CharField(max_length=64, help_text='Введите название: ')
    description = models.TextField(max_length=256, help_text='Введите описапние: ')


class Integrale(models.Model):
    weight = models.IntegerField(help_text='Введите вес: ')
    unit = models.CharField(max_length=2,
                            choices=MASS,
                            help_text='Введите еденицу измерения: '
                            )
    price = models.IntegerField(help_text='Введите сумму')
    name = models.CharField(max_length=64, help_text='Введите название: ')
    description = models.TextField(max_length=256, help_text='Введите описапние: ')

class Espresso(models.Model):
    weight = models.IntegerField(help_text='Введите вес: ')
    unit = models.CharField(max_length=2,
                            choices=MASS,
                            help_text='Введите еденицу измерения: '
                            )
    price = models.IntegerField(help_text='Введите сумму')
    name = models.CharField(max_length=64, help_text='Введите название: ')
    description = models.TextField(max_length=256, help_text='Введите описапние: ')

class Drip(models.Model):
    weight = models.IntegerField(help_text='Введите вес: ')
    unit = models.CharField(max_length=2,
                            choices=MASS,
                            help_text='Введите еденицу измерения: '
                            )
    price = models.IntegerField(help_text='Введите сумму')
    name = models.CharField(max_length=64, help_text='Введите название: ')
    description = models.TextField(max_length=256, help_text='Введите описапние: ')


class Catalog(models.Model):
    drip = models.OneToOneField(Drip, on_delete=models.CASCADE)
    espresso = models.OneToOneField(Espresso, on_delete=models.CASCADE)
    integrale = models.OneToOneField(Integrale, on_delete=models.CASCADE)
    speciale = models.OneToOneField(Speciale, on_delete=models.CASCADE)
    regular = models.OneToOneField(Regular, on_delete=models.CASCADE)

    def __str__(self):
        return self.name