from django.db import models
from django.contrib.auth import get_user_model


user = get_user_model()


score_choice = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
]


class ReviewModel(models.Model):
    score = models.CharField(choices=score_choice, null=True, blank=True, verbose_name="Оценка", max_length=1)
    usluga_name = models.TextField(null=True, blank=True, verbose_name="Название услуги")
    comment = models.TextField(null=True, blank=True, verbose_name="Комментарий")
    user = models.ForeignKey(user, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
