from django.contrib import admin

from .models import *  # noqa


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'requestid',
        'surname_ua',
        'first_name_ua',
        'negative_status'
    )
    ordering = ('-last_update', )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('when', 'provider', 'event')
    list_filter = ('subject', )
    ordering = ('-when', )


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'type_id', 'street_ua')
    list_filter = ('subject', )


@admin.register(Collateral)
class CollateralAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'contractid', 'type_id', 'value')
    list_filter = ('subject', )


@admin.register(Communication)
class CommunicationAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'type_id', 'value')
    list_filter = ('subject', )


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = (
        'id',
        'roleId',
        'contractid',
        'phase_id',
        'date_of_signature',
        'total_amount',
        'overdue_amount'
    )
    list_filter = ('subject', )
    ordering = ('-last_update', )


@admin.register(Dependant)
class DependantAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'type_id', 'count')
    list_filter = ('subject', )


@admin.register(EDR)
class EDRAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'state', 'state_text')
    list_filter = ('subject', )


@admin.register(ERBCheckup)
class ERBCheckupAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'data_register', 'status_code', 'status')
    list_filter = ('subject', )


@admin.register(Identification)
class IdentificationAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'type_id', 'number', 'expiration_date')
    list_filter = ('subject', )


@admin.register(MonthlyIncome)
class MonthlyIncomeAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'value', 'currency')
    list_filter = ('subject', )


@admin.register(MVSCheckup)
class MVSCheckupAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'data_register', 'status_code', 'status')
    list_filter = ('subject', )


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = (
        'id', 'contractid', 'accounting_date', 'rest_amount', 'overdue_amount'
    )
    list_filter = ('subject', )


@admin.register(Scoring)
class ScoringAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'degree', 'score', 'fault_chance', 'adverse')
    list_filter = ('subject', )


@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    raw_id_fields = ('subject', )
    list_display = ('id', 'category', 'value', 'code', 'count', 'amount')
    list_filter = ('subject', )


@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('code', 'value_ua', 'value_ru', 'dav', 'model_fields', )
