from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Evento


class EventoAdminForm(forms.ModelForm):
    descricao = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Evento
        fields = '__all__'


class EventoAdmin(admin.ModelAdmin):
    form = EventoAdminForm


admin.site.register(Evento, EventoAdmin)
