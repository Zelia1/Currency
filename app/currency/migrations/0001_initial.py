import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('status_code', models.CharField(max_length=3)),
                ('create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('code_name', models.CharField(max_length=64, unique=True)),
                ('url', models.CharField(max_length=255)),
                ('email_from', models.CharField(max_length=60)),
                ('number_phone', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=64)),
                ('message', models.CharField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'USD'), (1, 'EUR')])),
                ('sale', models.DecimalField(decimal_places=2, max_digits=5)),
                ('buy', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currency.banks')),
            ],
        ),
    ]
