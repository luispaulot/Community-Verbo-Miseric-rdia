from django.contrib import admin
from django import forms


from .models import PedidosOracao
from ckeditor.widgets import CKEditorWidget


class SobreAdminForm(forms.ModelForm):
    oracao = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PedidosOracao
        fields = '__all__'


class PedidosOracaoAdmin(admin.ModelAdmin):
    form = SobreAdminForm
    list_display = (
            'data',
            'nome',
            'cidade',
            'estado',
            'concluido'
            )
    ordering = ('-data',)

    search_fields = (
            'nome',
            'data'
            )
    list_per_page = 30

admin.site.register(PedidosOracao, PedidosOracaoAdmin)
