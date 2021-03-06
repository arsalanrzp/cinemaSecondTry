# Generated by Django 3.2.2 on 2021-05-15 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketing', '0003_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_count', models.IntegerField(max_length=10)),
                ('order_time', models.DateTimeField(auto_now_add=True)),
                ('costumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
                ('sans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketing.showtime')),
            ],
        ),
    ]
