# Generated by Django 3.1.3 on 2020-11-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainmaterials',
            name='unit',
            field=models.CharField(choices=[('Nos', 'Nos'), ('Kms', 'Kms'), ('Mtr', 'Mtr'), ('Set', 'Set'), ('Per Kit', 'Per Kit'), ('Cmtrs', 'Cmtrs'), ('Job', 'Job'), ('Mtrs', 'Mtrs'), ('Ft', 'Ft')], default='Nos', max_length=10),
        ),
    ]
