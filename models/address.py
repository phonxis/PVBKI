from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Address(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_addresses',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    type_id = models.IntegerField(
        _('Тип'),
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

    class Meta:
        verbose_name = _("Адрес")
        verbose_name_plural = _("Адреса")

    def __str__(self):
        return str(self.id)
