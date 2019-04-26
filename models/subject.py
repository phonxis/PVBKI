from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subject(models.Model):
    requestid = models.TextField(
        _('ID запроса'),
        blank=True
    )
    last_update = models.DateTimeField(
        _('Дата последнего обновления'),
        blank=True,
        null=True
    )
    entity = models.TextField(
        _('Сущность'),
        blank=True
    )
    gender = models.IntegerField(
        _('Пол'),
        blank=True,
        null=True
    )
    surname_ua = models.TextField(
        _('Фамилия'),
        help_text=_('(УКР)'),
        blank=True
    )
    surname_ru = models.TextField(
        _('Фамилия'),
        help_text=_('(РУС)'),
        blank=True
    )
    surname_en = models.TextField(
        _('Фамилия'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    first_name_ua = models.TextField(
        _('Имя'),
        help_text=_('(УКР)'),
        blank=True
    )
    first_name_ru = models.TextField(
        _('Имя'),
        help_text=_('(РУС)'),
        blank=True
    )
    first_name_en = models.TextField(
        _('Имя'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    fathers_name_ua = models.TextField(
        _('Отчество'),
        help_text=_('(УКР)'),
        blank=True
    )
    fathers_name_ru = models.TextField(
        _('Отчество'),
        help_text=_('(РУС)'),
        blank=True
    )
    fathers_name_en = models.TextField(
        _('Отчество'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    classification = models.IntegerField(
        _('Класификация'),
        blank=True,
        null=True
    )
    birth_surname_ua = models.TextField(
        _('Фамилия при рождении'),
        help_text=_('(УКР)'),
        blank=True
    )
    birth_surname_ru = models.TextField(
        _('Фамилия при рождении'),
        help_text=_('(РУС)'),
        blank=True
    )
    birth_surname_en = models.TextField(
        _('Фамилия при рождении'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    date_of_birth = models.DateTimeField(
        _('Дата рождения'),
        blank=True,
        null=True
    )
    place_of_birth_ua = models.TextField(
        _('Место рождения'),
        help_text=_('(УКР)'),
        blank=True
    )
    place_of_birth_ru = models.TextField(
        _('Место рождения'),
        help_text=_('(РУС)'),
        blank=True
    )
    place_of_birth_en = models.TextField(
        _('Место рождения'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    residency = models.IntegerField(
        _('Место жительства'),
        blank=True,
        null=True
    )
    citizenship = models.CharField(
        _('Гражданство'),
        max_length=16,
        blank=True
    )
    negative_status = models.IntegerField(
        _('Негативный статус'),
        blank=True,
        null=True
    )
    education = models.IntegerField(
        _('Образование'),
        blank=True,
        null=True
    )
    marital_status = models.IntegerField(
        _('Семейное положение'),
        blank=True,
        null=True
    )
    name_ua = models.TextField(
        _('Название'),
        help_text=_('(УКР)'),
        blank=True
    )
    name_ru = models.TextField(
        _('Название'),
        help_text=_('(РУС)'),
        blank=True
    )
    name_en = models.TextField(
        _('Название'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    abbreviation_ua = models.TextField(
        _('Аббревиатура'),
        help_text=_('(УКР)'),
        blank=True
    )
    abbreviation_ru = models.TextField(
        _('Аббревиатура'),
        help_text=_('(РУС)'),
        blank=True
    )
    abbreviation_en = models.TextField(
        _('Аббревиатура'),
        help_text=_('(АНГЛ)'),
        blank=True
    )
    ownership = models.IntegerField(
        _('Форма собственности'),
        blank=True,
        null=True
    )
    registration_date = models.DateTimeField(
        _('Дата регистрации'),
        blank=True,
        null=True
    )
    economic_activity = models.IntegerField(
        _('Экономическая деятельность'),
        blank=True,
        null=True
    )
    employee_count = models.IntegerField(
        _('Количество сотрудников'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _("Субъект")
        verbose_name_plural = _("Субъекты")

    def __str__(self):
        return str(self.requestid)
