# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('phtitle', models.CharField(unique=True, max_length=128)),
                ('phauthor', models.CharField(max_length=255)),
                ('phsite', models.CharField(max_length=255)),
                ('phnotes', models.TextField(help_text='Notes about photo')),
                ('phimage', models.ImageField(upload_to='photos')),
                ('phtime_registered', models.DateTimeField(auto_now=True)),
                ('phuser', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=u'id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
