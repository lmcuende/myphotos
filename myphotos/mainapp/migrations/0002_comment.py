# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                (u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ForeignKey(to='mainapp.Photo', to_field=u'id')),
                ('text', models.TextField(help_text='Your comment', verbose_name='Comment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
