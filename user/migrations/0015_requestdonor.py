# Generated by Django 3.1.6 on 2021-05-19 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_delete_requestdonor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDonor',
            fields=[
                ('requestDonorID', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('donorBloodType', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
                ('attachmentsDonor', models.FileField(upload_to='')),
                ('isApproved', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
