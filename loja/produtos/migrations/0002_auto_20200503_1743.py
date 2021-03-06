# Generated by Django 3.0.5 on 2020-05-03 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produto',
            options={},
        ),
        migrations.CreateModel(
            name='CompraEfetuada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
