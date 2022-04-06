# Generated by Django 4.0.3 on 2022-04-05 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name of Author')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Descriptin')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name of Publication')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('published_at', models.DateField()),
                ('visible_content', models.TextField(blank=True, null=True, verbose_name='Content to be Shown')),
                ('price', models.FloatField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page_app.author')),
                ('published_by', models.ManyToManyField(null=True, to='page_app.publication')),
            ],
        ),
    ]
