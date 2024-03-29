# Generated by Django 3.1.7 on 2021-04-24 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_un', models.EmailField(max_length=254)),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('pin', models.IntegerField()),
                ('phone', models.CharField(max_length=10)),
                ('psw', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_un', models.EmailField(max_length=254)),
                ('prod_cat', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cost', models.IntegerField()),
                ('qtn', models.IntegerField(default=1)),
                ('image', models.ImageField(upload_to='images/')),
                ('note', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=200)),
                ('g_map', models.TextField()),
                ('pin', models.IntegerField()),
                ('s_phone', models.CharField(max_length=10)),
                ('uname', models.EmailField(max_length=254, unique=True)),
                ('psw', models.CharField(max_length=10)),
                ('s_cat', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_s_un', models.EmailField(max_length=254)),
                ('p_c_n', models.CharField(max_length=200)),
                ('p_name', models.CharField(max_length=200)),
                ('p_qtn', models.IntegerField()),
                ('p_deliver', models.IntegerField()),
                ('p_cost', models.IntegerField()),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuickServiceApp.client')),
            ],
        ),
    ]
