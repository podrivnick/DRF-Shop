# Generated by Django 5.1 on 2024-08-14 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('name_receiver', models.CharField(max_length=50, verbose_name='Имя получателя')),
                ('phone_number', models.CharField(max_length=22, verbose_name='Номер телефона')),
                ('required_delivery', models.BooleanField(default=True, verbose_name='Требуется доставка')),
                ('delivery_address', models.CharField(max_length=100, verbose_name='Место доставки')),
                ('payment_on_get', models.BooleanField(default=True, verbose_name='Оплата при получении')),
                ('has_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.TextField(default='Обрабатывается', max_length=40, verbose_name='Статус заказа')),
                ('email', models.EmailField(max_length=80, verbose_name='Почта')),
                ('total_price', models.DecimalField(decimal_places=3, default=0, max_digits=17, verbose_name='Общая стоимость')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrdersItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Заказанный товар',
                'verbose_name_plural': 'Заказанные товары',
                'db_table': 'orders_item',
            },
        ),
    ]