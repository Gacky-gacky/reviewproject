# Generated by Django 3.0.4 on 2021-02-09 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('images', models.ImageField(upload_to='')),
                ('useful_review', models.IntegerField(blank=True, default=0, null=True)),
                ('useful_review_recoad', models.TextField()),
                ('evaluation', models.CharField(choices=[('良い', '良い'), ('悪い', '悪い')], max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
