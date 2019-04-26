from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Dependant(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_dependants',
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
    count = models.IntegerField(
        _('Количество'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Dependant")
        verbose_name_plural = _("Dependants")

    def __str__(self):
        return str(self.id)
