from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import (
    BannerPrincipal, Sobre, Contato, PedidoOracao, CalendarioSemanal,
    Vocacional, CalendarioSemanalImagem, Baluartes,
    Socio, Casas)


class CasasAdminForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Casas
        fields = '__all__'


class CasasAdmin(admin.ModelAdmin):
    form = CasasAdminForm


class SocioAdminForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Socio
        fields = '__all__'


class SocioAdmin(admin.ModelAdmin):
    form = SocioAdminForm


class BaluarteAdminForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Baluartes
        fields = '__all__'


class BaluarteAdmin(admin.ModelAdmin):
    form = BaluarteAdminForm


class VocacionalAdminForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Vocacional
        fields = '__all__'


class VocacionalAdmin(admin.ModelAdmin):
    form = VocacionalAdminForm


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
admin.site.register(Vocacional, VocacionalAdmin)
admin.site.register(CalendarioSemanalImagem)
admin.site.register(Baluartes, BaluarteAdmin)
admin.site.register(Socio, SocioAdmin)
admin.site.register(Casas, CasasAdmin)
