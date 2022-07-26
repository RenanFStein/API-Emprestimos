# Generated by Django 4.0.6 on 2022-07-08 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emprestimos', '0005_tabelataxas_parcelas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juros_parcela', models.DecimalField(decimal_places=10, max_digits=19)),
                ('valor_juros_parcelado', models.DecimalField(decimal_places=10, max_digits=19)),
                ('comissao', models.DecimalField(decimal_places=10, max_digits=19)),
                ('valor_comissao', models.DecimalField(decimal_places=10, max_digits=19)),
                ('valor_parcela', models.DecimalField(decimal_places=10, max_digits=19)),
                ('numero_cartao', models.DecimalField(decimal_places=0, max_digits=30)),
                ('valor_desejado', models.DecimalField(decimal_places=10, max_digits=19)),
                ('total_emprestimo', models.DecimalField(decimal_places=10, max_digits=19)),
                ('id_cliente_banco', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emprestimos.cliente')),
                ('id_parcela', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emprestimos.parcelas')),
                ('id_tabela_taxas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emprestimos.tabelataxas')),
            ],
        ),
    ]