# Generated by Django 4.0.3 on 2022-03-11 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fa', models.CharField(max_length=100)),
                ('background_color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('has_available_products', models.BooleanField()),
                ('is_open', models.BooleanField()),
                ('rate', models.IntegerField()),
                ('rate_count', models.IntegerField()),
                ('service_radius', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_fa', models.CharField(max_length=100)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dk.category')),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dk.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dk.shop')),
                ('shop_product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dk.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dk.user')),
            ],
        ),
    ]
