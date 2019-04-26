from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Event(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_events',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    provider = models.IntegerField(
        _('Провайдер'),
        blank=True,
        null=True
    )
    event = models.CharField(
        _('Событие'),
        max_length=16,
        blank=True
    )
    when = models.DateTimeField(
        _('Дата события'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return str(self.id)
