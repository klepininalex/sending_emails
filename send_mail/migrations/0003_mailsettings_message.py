# Generated by Django 4.2.4 on 2023-09-17 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_mail', '0002_mailsettings_alter_client_comment_alter_client_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsettings',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='send_mail.textmail', verbose_name='сообщение'),
        ),
    ]
