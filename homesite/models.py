import os
import uuid

from django.db import models


def rename_banner(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/banner/'+file+'.'+ext
    return name


def rename_sobre(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/sobre/'+file+'.'+ext
    return name


def rename_pedidos_oracao(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/pedido_oracao/'+file+'.'+ext
    return name


class BannerPrincipal(models.Model):
    mensagem1 = models.CharField('Mensagem 1', max_length=500)
    mensagem2 = models.CharField('Mensagem 2', max_length=500)
    imagem = models.ImageField(
        'Imagem', upload_to=rename_banner, blank=False, null=False, help_text='1500x760')

    class Meta:
        verbose_name = "Banner Principal"
        verbose_name_plural = "Banner Principal"

    def __str__(self):
        return self.mensagem1


class Sobre(models.Model):
    titulo = models.CharField(
        'Título', max_length=200, blank=False, null=False)
    texto = models.CharField(
        'Texto', max_length=9000, blank=False, null=False)
    imagem = models.ImageField(
        'Imagem', upload_to=rename_sobre, blank=False, null=False, help_text='750x400')

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Sobre"

    def __str__(self):
        return self.titulo


class Contato(models.Model):
    logradouro = models.CharField(
        'Logradouro', max_length=100, blank=False, null=False)
    numero = models.IntegerField(
        'Numero')
    complemento = models.CharField(
        'Complemento', max_length=100, blank=True, null=True)
    bairro = models.CharField(
        'Bairro', max_length=100, blank=True, null=True)
    cidade = models.CharField(
        'Cidade', max_length=100, blank=False, null=False)
    estado = models.CharField(
        'Estado', max_length=50, blank=False, null=False)
    cep = models.CharField('CEP', max_length=50)
    telefone1 = models.CharField('Telefone 1', max_length=14)
    telefone2 = models.CharField('Telefone 2', max_length=14)
    email = models.EmailField('Email')
    latitude = models.CharField('Latitude', max_length=20, blank=True, null=True)
    longitude = models.CharField('Longitude', max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contato"

    def __str__(self):
        return 'Endereço, telefone e email'

    def endereco(self):
        if self.complemento:
            endereco = self.logradouro + ', ' + str(self.numero) + ' - '+ self.complemento +', '+ self.bairro +  '<br>' + self.cidade + ' - '+self.estado
        else:
            endereco = self.logradouro + ', ' + str(self.numero) +', '+ self.bairro +  '<br>' + self.cidade + ' - '+self.estado
        return endereco

    def telefones(self):
        if self.telefone2:
            return self.telefone1 + ' | ' + self.telefone2
        else:
            return self.telefone1


class PedidoOracao(models.Model):
    titulo = models.CharField('Título', max_length=50, blank=False, null=False)
    texto = models.CharField('Texto', max_length=1000, blank=False, null=False)
    imagem = models.ImageField(
        'Imagem', upload_to=rename_pedidos_oracao, blank=False, null=False, help_text='1500x610')
    texto_botao = models.CharField('Texto', max_length=50, blank=False, null=False)
    mensagem_resposta_automatica = models.CharField(
        'Resposta automática', max_length=10000, blank=False, null=False)

    class Meta:
        verbose_name = "Pedido de oração"
        verbose_name_plural = "Pedido de oração"

    def __str__(self):
        return 'Área pedidos de oração'


DIA_CHOICES = (
    ('Segunda-feira', 'Segunda'),
    ('Terça-feira', 'Terça'),
    ('Quarta-feira', 'Quarta'),
    ('Quinta-feira', 'Quinta'),
    ('Sexta-feira', 'Sexta'),
    ('Sabado', 'Sábado'),
    ('Domingo', 'Domingo'),
    )


class CalendarioSemanal(models.Model):
    dia = models.CharField(
        'Dia 1', max_length=50, choices=DIA_CHOICES, blank=False, null=False)
    titulo = models.CharField('Título', max_length=50, blank=False, null=False)
    horario_inicial = models.TimeField('Horário inicial')
    horario_final = models.TimeField('Horário inicial')
    texto = models.CharField('Texto', max_length=1000)

    def __str__(self):
        return '{}'.format(self.dia) 