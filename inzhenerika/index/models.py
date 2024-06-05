from django.db import models
class Consult(models.Model):
    class Meta:
        verbose_name = "Консультация"
        verbose_name_plural = "Консультации"

    fio = models.CharField('ФИО', max_length=255)
    phone = models.CharField('Телефон', max_length=18)
    description = models.TextField('Описание')
    date_consult = models.DateField('Дата', auto_now=True)

    def __str__(self):
        return f'{self.date_consult}, {self.phone}, {self.fio}'