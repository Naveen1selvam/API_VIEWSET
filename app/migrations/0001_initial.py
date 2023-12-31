# Generated by Django 4.2.2 on 2023-06-15 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=100)),
                ('cid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pname', models.CharField(max_length=100)),
                ('Pid', models.IntegerField()),
                ('PriceP', models.IntegerField()),
                ('Cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcategory')),
            ],
        ),
    ]
