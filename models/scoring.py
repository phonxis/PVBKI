from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Scoring(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_scoring',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    degree = models.CharField(
        _('Оценка'),
        max_length=16,
        blank=True
    )
    score = models.IntegerField(
        _('Рейтинг'),
        blank=True,
        null=True
    )
    fault_chance = models.DecimalField(
        _('Вероятность дефолта'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    adverse = models.IntegerField(
        _('Adverse'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Scoring")
        verbose_name_plural = _("Scoring")

    def __str__(self):
        return str(self.id)
