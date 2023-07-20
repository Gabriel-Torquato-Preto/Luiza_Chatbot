# Generated by Django 4.2.3 on 2023-07-20 19:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_resposta_delete_respostas_alter_luiza_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='reposta',
            new_name='resposta',
        ),
        migrations.AlterField(
            model_name='luiza',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cc57b8a1-03c3-4380-99a5-9b2aa82f632e'), primary_key=True, serialize=False),
        ),
    ]
