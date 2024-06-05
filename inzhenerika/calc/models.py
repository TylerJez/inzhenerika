from django.db import models

class Calc(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    fio = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=18)
    name_job = models.CharField('Название работ', max_length=255)
    adress = models.CharField('Адрес', max_length=255)
    date_order = models.DateField('Дата', auto_now=True)

    def __str__(self):
        return f'{self.date_order}, {self.phone}, {self.fio}, {self.name_job}, {self.adress}'
