# Generated by Django 2.1.2 on 2018-11-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(default='abc123@mail.ru', max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('director', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('lastname', models.CharField(default='', max_length=255, verbose_name='Фамилия')),
                ('firstname', models.CharField(default='', max_length=255, verbose_name='Имя')),
                ('secondname', models.CharField(default='', max_length=255, null=True, verbose_name='Отчество')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('company', models.CharField(default='', max_length=100, verbose_name='компания')),
                ('old_pass', models.BooleanField(default=True)),
                ('image', models.FileField(default='person.jpg', upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
