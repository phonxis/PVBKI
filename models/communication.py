from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Communication(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_communications',
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
    value = models.TextField(
        _('Номер'),
        blank=True
    )

    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакты")

    def __str__(self):
        return str(self.id)
