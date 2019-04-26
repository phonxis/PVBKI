from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class EDR(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_edr',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    state = models.TextField(
        _('State'),
        blank=True
    )
    state_text = models.TextField(
        _('State'),
        blank=True
    )

    class Meta:
        verbose_name = _("EDR")
        verbose_name_plural = _("EDR")

    def __str__(self):
        return str(self.id)
