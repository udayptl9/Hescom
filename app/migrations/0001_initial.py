# Generated by Django 3.1.3 on 2020-11-02 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainMaterials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular', models.CharField(max_length=250)),
                ('unit', models.CharField(choices=[('Nos', 'Nos'), ('Kms', 'Kms'), ('Mtr', 'Mtr'), ('Set', 'Set')], default='Nos', max_length=10)),
                ('material_rate', models.CharField(max_length=50)),
                ('labour_rate', models.CharField(max_length=50)),
            ],
        ),
    ]
