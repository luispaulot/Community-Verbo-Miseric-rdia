from django.conf.locale.pt_BR import formats as pt_formats

from django.contrib import admin
from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import LectioDivina

pt_formats.DATETIME_FORMAT = "d M Y H:i:s"


class LectioDivinaAdminForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = LectioDivina
        fields = '__all__'


class LectioDivinaAdmin(admin.ModelAdmin):
    form = LectioDivinaAdminForm

admin.site.register(LectioDivina, LectioDivinaAdmin)
