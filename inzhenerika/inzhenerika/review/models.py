from django.db import models

SCORE = [
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
]

class Review(models.Model):
    score = models.CharField('Оценка', choices=SCORE, max_length=5)
    fio = models.CharField('ФИО',max_length=255)
    comment = models.TextField('Комментарий')
    date_review = models.DateField('Дата', auto_now=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f'{self.score}, {self.date_review}, {self.fio}'