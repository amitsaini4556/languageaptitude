# Generated by Django 2.2.10 on 2020-05-06 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cpp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quizname', models.TextField(max_length=10)),
                ('question', models.TextField(max_length=500)),
                ('code', models.TextField(max_length=1000)),
                ('op1', models.TextField(max_length=100)),
                ('op2', models.TextField(max_length=100)),
                ('op3', models.TextField(max_length=100)),
                ('op4', models.TextField(max_length=100)),
                ('answer', models.TextField(max_length=100)),
                ('solution', models.TextField(max_length=500)),
            ],
        ),
    ]