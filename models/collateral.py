from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Collateral(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_collaterals',
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
    type_id = models.IntegerField(
        _('Тип'),
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
    address_type_id = models.IntegerField(
        _('Тип адреса'),
        blank=True,
        null=True
    )
    location_id = models.IntegerField(
        _('Локация'),
        blank=True,
        null=True
    )
    street_ua = models.TextField(
        _('Адрес'),
        help_text=_('(УКР)'),
        blank=True
    )
    street_ru = models.TextField(
        _('Адрес'),
        help_text=_('(РУС)'),
        blank=True
    )
    street_en = models.TextField(
        _('Адрес'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    postal_code = models.CharField(
        _('Индекс'),
        max_length=16,
        blank=True
    )
    identification_type_id = models.IntegerField(
        _('Тип документа'),
        blank=True,
        null=True
    )
    number = models.TextField(
        _('Номер'),
        blank=True
    )
    registrationDate = models.DateTimeField(
        _('Дата регистрации'),
        blank=True,
        null=True
    )
    issueDate = models.DateTimeField(
        _('Дата выдачи'),
        blank=True,
        null=True
    )
    expirationDate = models.DateTimeField(
        _('Дата окончания срока годности'),
        blank=True,
        null=True
    )
    authority_ua = models.TextField(
        _('Кем выдан'),
        help_text=_('(УКР)'),
        blank=True
    )
    authority_ru = models.TextField(
        _('Кем выдан'),
        help_text=_('(РУС)'),
        blank=True
    )
    authority_en = models.TextField(
        _('Кем выдан'),
        help_text=_('(АНГЛ)'),
        blank=True
    )

    class Meta:
        verbose_name = _("Collateral")
        verbose_name_plural = _("Collaterals")

    def __str__(self):
        return str(self.id)
