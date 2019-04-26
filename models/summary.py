from django.db import models
from django.utils.translation import ugettext_lazy as _

from .subject import Subject


class Summary(models.Model):
    subject = models.ForeignKey(
        Subject,
        related_name='pvbki_summaries',
        verbose_name=_('Субъект'),
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    category = models.CharField(
        _('Категория'),
        max_length=32,
        blank=True
    )
    value = models.IntegerField(
        _('Значение'),
        blank=True,
        null=True
    )
    code = models.CharField(
        _('Код'),
        max_length=32,
        blank=True
    )
    count = models.IntegerField(
        _('Количество'),
        blank=True,
        null=True
    )
    amount = models.DecimalField(
        _('Сумма'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Итог")
        verbose_name_plural = _("Итоги")

    def __str__(self):
        return str(self.id)
