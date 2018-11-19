# Generated by Django 2.1.3 on 2018-11-19 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.Grado')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pensum.Materia')),
            ],
        ),
        migrations.AddField(
            model_name='grado',
            name='materias',
            field=models.ManyToManyField(through='pensum.Seccion', to='pensum.Materia'),
        ),
    ]