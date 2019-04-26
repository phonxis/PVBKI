from django.db import models
from django.utils.translation import ugettext_lazy as _


class Vocabulary(models.Model):
    code = models.CharField(
        _('Код'),
        max_length=16
    )
    value_ua = models.TextField(
        _('Значение (UA)'),
        blank=True
    )
    value_ru = models.TextField(
        _('Значение (RU)'),
        blank=True
    )
    value_en = models.TextField(
        _('Значение (EN)'),
        blank=True
    )
    dav = models.CharField(
        _('DAV'),
        max_length=16
    )
    model_fields = models.TextField(
        _('Поля моделей'),
    )

    class Meta:
        verbose_name = _("Словарь")
        verbose_name_plural = _("Словарь")

    def __str__(self):
        return "{0}: {1}".format(self.dav, self.code)
