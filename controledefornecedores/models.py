from django.db import models

class Controle(models.Model):
    nome = models.CharField('Nome', max_length=30, null=True,blank=True)
    CNPJ = models.PositiveIntegerField('CNPJ',null=True,blank=True)
    endereco = models.CharField('Endereço',max_length=30,null=True,blank=True)
    TIPO = ((1, 'Ativo'),(2, 'Inativo'))
    tipo = models.PositiveIntegerField(verbose_name='Tipo', choices= TIPO)

    def __str__(self):
        return self.nome
