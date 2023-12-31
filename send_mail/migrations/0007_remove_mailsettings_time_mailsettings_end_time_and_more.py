# Generated by Django 4.2.4 on 2023-09-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0006_alter_textmail_body_alter_textmail_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailsettings',
            name='time',
        ),
        migrations.AddField(
            model_name='mailsettings',
            name='end_time',
            field=models.TimeField(default='00:00', verbose_name='время окончания рассылки'),
        ),
        migrations.AddField(
            model_name='mailsettings',
            name='start_time',
            field=models.TimeField(default='09:00', verbose_name='время старта рассылки'),
        ),
    ]
