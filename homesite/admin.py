from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import (
    BannerPrincipal, Sobre, Contato, PedidoOracao, CalendarioSemanal)


class SobreAdminForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Sobre
        fields = '__all__'


class SobreAdmin(admin.ModelAdmin):
    form = SobreAdminForm


class PedidoOracaoForm(forms.ModelForm):
    mensagem_resposta_automatica = forms.CharField(widget=CKEditorWidget())
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PedidoOracao
        fields = '__all__'


class PedidoOracaoAdmin(admin.ModelAdmin):
    form = PedidoOracaoForm


admin.site.register(BannerPrincipal)
admin.site.register(CalendarioSemanal)
admin.site.register(Sobre, SobreAdmin)
admin.site.register(PedidoOracao, PedidoOracaoAdmin)
admin.site.register(Contato)
