# Generated by Django 3.2.7 on 2021-09-25 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20210925_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='idConversacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.conversacion'),
        ),
    ]
