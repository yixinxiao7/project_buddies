from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=1000)),
                ('team_leader', models.CharField(max_length=100)),
                ('team_info', models.CharField(max_length=100000)),
                ('team_progress', models.DecimalField(decimal_places=2,max_digits=5)),
                ('team_picture', models.BinaryField()),
            ],
        ),
    ]