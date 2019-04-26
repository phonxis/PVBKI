from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class ERBCheckup(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_erb',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    data_register = models.IntegerField(
        _('Data Register'),
        blank=True,
        null=True
    )
    status_code = models.IntegerField(
        _('Код статуса'),
        blank=True,
        null=True
    )
    status = models.TextField(
        _('Статус'),
        blank=True
    )

    class Meta:
        verbose_name = _("ERBCheckup")
        verbose_name_plural = _("ERBCheckup")

    def __str__(self):
        return str(self.id)
