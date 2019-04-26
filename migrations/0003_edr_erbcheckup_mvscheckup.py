# Generated by Django 2.1.4 on 2019-02-25 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pvbki', '0002_auto_20190225_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='EDR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.TextField(blank=True, verbose_name='State')),
                ('state_text', models.TextField(blank=True, verbose_name='State')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pvbki_edr', to='pvbki.Subject', verbose_name='Субъект')),
            ],
            options={
                'verbose_name_plural': 'EDR',
                'verbose_name': 'EDR',
            },
        ),
        migrations.CreateModel(
            name='ERBCheckup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_register', models.IntegerField(blank=True, null=True, verbose_name='Data Register')),
                ('status_code', models.IntegerField(blank=True, null=True, verbose_name='Код статуса')),
                ('status', models.TextField(blank=True, verbose_name='Статус')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pvbki_erb', to='pvbki.Subject', verbose_name='Субъект')),
            ],
            options={
                'verbose_name_plural': 'ERBCheckup',
                'verbose_name': 'ERBCheckup',
            },
        ),
        migrations.CreateModel(
            name='MVSCheckup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_register', models.IntegerField(blank=True, null=True, verbose_name='Data Register')),
                ('status_code', models.IntegerField(blank=True, null=True, verbose_name='Код статуса')),
                ('status', models.TextField(blank=True, verbose_name='Статус')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pvbki_mvs', to='pvbki.Subject', verbose_name='Субъект')),
            ],
            options={
                'verbose_name_plural': 'MVSCheckup',
                'verbose_name': 'MVSCheckup',
            },
        ),
    ]