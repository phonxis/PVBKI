from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Identification(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_identifications',
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
    number = models.TextField(
        _('Номер'),
        blank=True
    )
    registration_date = models.DateTimeField(
        _('Дата регистрации'),
        blank=True,
        null=True
    )
    issue_date = models.DateTimeField(
        _('Дата выдачи'),
        blank=True,
        null=True
    )
    expiration_date = models.DateTimeField(
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
        verbose_name = _("Идентификационный документ")
        verbose_name_plural = _("Идентификационные документы")

    def __str__(self):
        return str(self.id)
