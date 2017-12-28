from django import forms

from pedidos_oracao.models import PedidosOracao


class EmailForm(forms.Form):
    nome = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control form-text',
        'type': 'text',
        'placeholder': 'Escreva seu nome aqui'
        }), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control form-text',
        'type': 'email',
        'placeholder': 'Escreva seu endereço de email aqui.'
        }), required=True)
    mensagem = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control form-text',
        'type': 'text',
        'rows': '8',
        'placeholder': 'Escreva a mensagem aqui.'
        }), required=True)


class PedidoOracaoForm(forms.Form):
    class Meta:
        model = PedidosOracao
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
            }),
            'oracao': forms.Textarea(attrs={
                'class': 'form-control',
            }),
            'estado': forms.Select(attrs={
                'class': 'form-control',
            }),
            'cidade': forms.TextInput(attrs={
                'class': 'form-control',
            }),
        }


class SocioForm(forms.Form):
    class Meta:
        email = forms.EmailField(label='Seu email', max_length=100)
        nome = forms.CharField(label='Seu nome completo', max_length=100)
