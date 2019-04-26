from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Record(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_records',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    contractid = models.IntegerField(
        _('ID договора'),
        blank=True,
        null=True
    )
    accounting_date = models.DateTimeField(
        _('Accounting Date'),
        blank=True,
        null=True
    )
    credit_usage = models.IntegerField(
        _('Использование кредита'),
        blank=True,
        null=True
    )
    rest_amount = models.DecimalField(
        _('Оставшаяся сумма'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    rest_currency = models.CharField(
        _('Валюта оставшейся суммы'),
        max_length=10,
        blank=True
    )
    rest_instalment_count = models.IntegerField(
        _('Оставшееся количество платежей'),
        blank=True,
        null=True
    )
    overdue_amount = models.DecimalField(
        _('Просроченная сумма'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    overdue_currencyoverdue_amount = models.DecimalField(
        _('Валюта просроченной суммы'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    overdue_countrest_instalment_count = models.IntegerField(
        _('Количество просроченных платежей'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Record")
        verbose_name_plural = _("Records")

    def __str__(self):
        return str(self.id)
