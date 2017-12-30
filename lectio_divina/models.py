import os
import uuid
from datetime import datetime

from django.db import models


def rename_lectio(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/lectio/images/'+file+'.'+ext
    return name


def rename_audio(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/lectio/audios/'+file+'.'+ext
    return name


class LectioDivina(models.Model):
    titulo = models.CharField('Título', max_length=50, blank=False, null=False)
    texto = models.CharField('Texto', max_length=10000, blank=False, null=False)
    data = models.DateField('Data', blank=False, null=False)
    audio = models.FileField(
        'Audio', upload_to=rename_audio, blank=True, null=False, help_text='Somente arquivos MP3')
    imagem = models.ImageField(
        'Imagem', upload_to=rename_lectio, blank=True, null=True, help_text='750x430')

    class Meta:
        verbose_name = "Lectio Divina"
        verbose_name_plural = "Lectio Divina"

    def __str__(self):
        return '{} - {}'.format(self.data, self.titulo)

    def save(self, *args, **kwargs):
        now = datetime.now()
        super(LectioDivina, self).save(*args, **kwargs)
