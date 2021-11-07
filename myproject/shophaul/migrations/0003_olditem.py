# Generated by Django 3.2.9 on 2021-11-07 21:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shophaul', '0002_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='OldItem',
            fields=[
                ('oitem_id', models.AutoField(primary_key=True, serialize=False)),
                ('oname', models.CharField(max_length=40)),
                ('oquantity', models.PositiveIntegerField(default=0)),
                ('oprice', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('oaddress', models.CharField(max_length=150)),
                ('oseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oseller_items', to='shophaul.seller')),
            ],
            options={
                'verbose_name': 'OldItem',
                'verbose_name_plural': 'OldItems',
                'db_table': 'old_items',
                'ordering': ['oitem_id'],
            },
        ),
    ]