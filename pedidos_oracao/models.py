from django.db import models


UF_CHOICES = (
    ('AC', 'Acre'),
    ('AL', 'Alagoas'),
    ('AP', 'Amapá'),
    ('BA', 'Bahia'),
    ('CE', 'Ceará'),
    ('DF', 'Distrito Federal'),
    ('ES', 'Espírito Santo'),
    ('GO', 'Goiás'),
    ('MA', 'Maranão'),
    ('MG', 'Minas Gerais'),
    ('MS', 'Mato Grosso do Sul'),
    ('MT', 'Mato Grosso'),
    ('PA', 'Pará'),
    ('PB', 'Paraíba'),
    ('PE', 'Pernanbuco'),
    ('PI', 'Piauí'),
    ('PR', 'Paraná'),
    ('RJ', 'Rio de Janeiro'),
    ('RN', 'Rio Grande do Norte'),
    ('RO', 'Rondônia'),
    ('RR', 'Roraima'),
    ('RS', 'Rio Grande do Sul'),
    ('SC', 'Santa Catarina'),
    ('SE', 'Sergipe'),
    ('SP', 'São Paulo'),
    ('TO', 'Tocantins')
)


class PedidosOracao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    nome = models.CharField('Nome', max_length=150, blank=False, null=False)
    email = models.EmailField('Email', blank=True, null=True)
    oracao = models.CharField('Oração', max_length=20000)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=50, choices=UF_CHOICES)
    concluido = models.BooleanField('Concluído', default=False)

    class Meta:
        verbose_name = "pedidos de oração"
        verbose_name_plural = "pedidos de oração"

    def __str__(self):
        return '{}'.format(self.data.strftime("%d-%m-%Y %H:%M:%S"))
