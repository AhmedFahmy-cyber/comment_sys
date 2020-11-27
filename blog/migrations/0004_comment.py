# Generated by Django 3.1.3 on 2020-11-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200404_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.CharField(max_length=500)),
                ('publish', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commnt_post', to='blog.post')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]