# Generated by Django 4.0.6 on 2022-07-07 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0004_rename_banco_bancocliente_cliente_banco_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TabelaTaxas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tabela', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Parcelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcela', models.DecimalField(decimal_places=10, max_digits=19)),
                ('juros_parcela', models.DecimalField(decimal_places=10, max_digits=19)),
                ('valor_parcela', models.DecimalField(decimal_places=10, max_digits=19)),
                ('valor_total', models.DecimalField(decimal_places=10, max_digits=19)),
                ('comissao', models.DecimalField(decimal_places=10, max_digits=19)),
                ('tabela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emprestimos.tabelataxas')),
            ],
        ),
    ]