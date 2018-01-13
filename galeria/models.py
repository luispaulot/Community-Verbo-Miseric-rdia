import os
import uuid


from django.db import models


def rename_foto(instance, filename):
    ext = filename.split(".")[-1]
    file = str(uuid.uuid4())
    name = 'uploads/fotos/'+file+'.'+ext
    return name


class Album(models.Model):
    titulo = models.CharField('Título', max_length=50, blank=False, null=False)
    data = models.DateField('Data')
    local = models.CharField('Local', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return '{} | album: {}'.format(self.data, self.titulo)


class Foto(models.Model):
    album = models.ForeignKey('Album', blank=False, null=False)
    imagem = models.ImageField(
        'Imagem', upload_to=rename_foto, blank=False, null=False)
    comentario = models.CharField(
        'Comentário', max_length=500, blank=True, null=True)
    capa = models.BooleanField('É capa do album?', default=False)

    class Meta:
        verbose_name = "Foto"
        verbose_name_plural = "Fotos"

    def __str__(self):
        return 'album: {}'.format(self.album)
