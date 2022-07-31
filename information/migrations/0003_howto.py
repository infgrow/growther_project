# Generated by Django 2.2 on 2022-07-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_auto_20220728_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowTo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=12, verbose_name='해시태그')),
                ('instruction_header', models.CharField(max_length=24, verbose_name='제목')),
                ('instruction_content', models.TextField(verbose_name='내용')),
                ('img_path', models.CharField(max_length=255, verbose_name='이미지 경로')),
            ],
        ),
    ]
