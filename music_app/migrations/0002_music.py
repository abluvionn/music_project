# Generated by Django 4.0.3 on 2022-03-30 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.IntegerField(default=3)),
                ('country', models.CharField(choices=[('KG', 'KYRGYZSTAN'), ('KZ', 'KAZAHSTAN')], max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='music', to='music_app.category')),
            ],
        ),
    ]
