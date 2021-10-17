# Generated by Django 3.2.7 on 2021-10-17 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0011_auto_20211017_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='idUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='chat.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
