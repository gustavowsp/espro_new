# Generated by Django 4.2.4 on 2023-08-08 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_vaga', models.CharField(max_length=25)),
                ('descricao_vaga', models.TextField()),
                ('foto_vaga', models.ImageField(upload_to='pictures/Y%/%m/%d')),
                ('salario_vaga', models.FloatField()),
                ('localidade_Vaga', models.CharField(max_length=60)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]