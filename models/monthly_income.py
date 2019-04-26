from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class MonthlyIncome(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_incomes',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    value = models.DecimalField(
        _('Значение'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    currency = models.CharField(
        _('Валюта'),
        max_length=10,
        blank=True
    )

    class Meta:
        verbose_name = _("Месячный доход")
        verbose_name_plural = _("Месячный доход")

    def __str__(self):
        return str(self.id)
