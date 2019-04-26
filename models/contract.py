from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Contract(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_contracts',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    roleId = models.IntegerField(
        _('Роль'),
        blank=True,
        null=True
    )
    provider = models.IntegerField(
        _('Провайдер'),
        blank=True,
        null=True
    )
    contractid = models.IntegerField(
        _('ID договора'),
        blank=True,
        null=True
    )
    last_update = models.DateTimeField(
        _('Дата обновления'),
        blank=True,
        null=True
    )
    phase_id = models.IntegerField(
        _('Фаза'),
        blank=True,
        null=True
    )
    currency = models.CharField(
        _('Валюта'),
        max_length=10,
        blank=True
    )
    date_of_signature = models.DateTimeField(
        _('Дата подписания'),
        blank=True,
        null=True
    )
    credit_purpose = models.IntegerField(
        _('Цель кредита'),
        blank=True,
        null=True
    )
    negative_status = models.IntegerField(
        _('Негативный статус'),
        blank=True,
        null=True
    )
    application_date = models.DateTimeField(
        _('Дата подачи заявки'),
        blank=True,
        null=True
    )
    start_date = models.DateTimeField(
        _('Дата начала'),
        blank=True,
        null=True
    )
    expected_end_date = models.DateTimeField(
        _('Предположительная дата окончания'),
        blank=True,
        null=True
    )
    factual_end_date = models.DateTimeField(
        _('Фактическая дата окончания'),
        blank=True,
        null=True
    )
    type = models.CharField(
        _('Тип'),
        max_length=16,
        blank=True
    )
    payment_method_id = models.IntegerField(
        _('Способ оплаты'),
        blank=True,
        null=True
    )
    payment_period_id = models.IntegerField(
        _('Период оплаты'),
        blank=True,
        null=True
    )
    actual_currency = models.CharField(
        _('Валюта'),
        max_length=10,
        help_text='actual currency',
        blank=True
    )
    total_amount = models.DecimalField(
        _('Итоговая сумма'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    credit_limit = models.DecimalField(
        _('Кредитный лимит'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    instalment_count = models.IntegerField(
        _('Количество платежей'),
        blank=True,
        null=True
    )
    instalment_amount_currency = models.CharField(
        _('Валюта взноса'),
        max_length=10,
        help_text='instalment amount currency',
        blank=True
    )
    instalment_amount = models.DecimalField(
        _('Сумма взноса'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    rest_instalment_count = models.IntegerField(
        _('Количество оставшихся платежей'),
        blank=True,
        null=True
    )
    rest_amount = models.DecimalField(
        _('Непогашенная сумма'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    overdue_count = models.IntegerField(
        _('Количество просроченных платежей'),
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

    class Meta:
        verbose_name = _("Договор")
        verbose_name_plural = _("Договора")

    def __str__(self):
        return str(self.id)
