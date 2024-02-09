from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator 

# Create your models here.


#Main catalog model
class Catalog(models.Model):
    MASS = [
        ('Kilogramms', 'Кг'),
        ('Gramms', 'Гр')
    ]

    SORT = [
        ('REGULAR', 'Regular'),
        ('SCPECIALE', 'Speciale'),
        ('INTEGRALE', 'Integrale'),
        ('ESPRESSO', 'Espresso'),
        ('DRIP', 'Drip')
    ]

    weight = models.IntegerField(help_text='Введите вес: ',
                                 verbose_name='Вес',
                                 unique=True)
    
    mass = models.CharField(max_length=64,
                            choices=MASS,
                            help_text='Выберете массу: ',
                            verbose_name='Масса',
                            unique=True)
    
    price = models.IntegerField(help_text='Введите сумму: ',
                                verbose_name='Цена',
                                unique=True)
    
    name = models.CharField(max_length=64,
                            help_text='Введите название: ',
                            verbose_name='Название',
                            unique=True)
    
    description = models.TextField(max_length=256,
                                    help_text='Введите описапние: ',
                                    verbose_name='Описание',
                                    unique=True)
    
    unit = models.CharField(max_length=9,
                            choices=SORT,
                            help_text='Выберете сорт: ',
                            verbose_name='Категория',
                            unique=True)
    
    def __str__(self):
        return self.name + ' ' + self.unit

#Order model
class Order(models.Model):
    STATUS = [
        ('NEW', 'Новый заказ'),
        ('WAIT_PAID', 'Ждут отплаты'),
        ('STARTED', 'В работе'),
        ('READY', 'Отгружен'),
    ]

    order_status = models.CharField(max_length=10,
                                    choices=STATUS,
                                    verbose_name="Статус",
                                    blank=False)
    order_catalog = models.ForeignKey(Catalog,
                                    on_delete=models.CASCADE,
                                    verbose_name='Товар',
                                    blank=False,)
    first_name = models.CharField(max_length=64,
                                   verbose_name="Имя",
                                    blank=False,)  
    last_name = models.CharField(max_length=64,
                                    verbose_name="Фамилия",
                                    blank=False,)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex],
                                    max_length = 16,
                                    unique = True,
                                    verbose_name='Номер телефона',
                                    default='89990001122')


    def save(self, *args, **kwargs):
        for field_name in ['first_name', 'last_name']:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Order, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('order-details', kwargs={'pk': self.pk})


    def __str__(self):
        return self.first_name.title() + ' ' + self.last_name.title()

