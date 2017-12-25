import os
import uuid

from django.db import models


def rename_evento_imagem(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/evento/'+file+'.'+ext
    return name


class Evento(models.Model):
    data_inicio = models.DateTimeField(
        'Data Início', blank=False, null=False)
    data_fim = models.DateTimeField(
        'Data Fim', blank=True, null=True)
    titulo = models.CharField(
        'Título do evento', max_length=100, blank=False, null=False)
    descricao = models.CharField(
        'Descrição', max_length=2000, blank=True, null=True)
    imagem = models.ImageField(
        'Imagem', upload_to=rename_evento_imagem, blank=True, null=True, help_text='to define')

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return 'Evento: {} - {}' .format(self.data_inicio, self.titulo)
