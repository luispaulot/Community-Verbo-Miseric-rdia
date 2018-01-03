from datetime import datetime

from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render

from django.views.generic import TemplateView, FormView

from lectio_divina.models import LectioDivina

from agenda.models import Evento
from pedidos_oracao.models import PedidosOracao
from galeria.models import Album, Foto

from .models import (
    BannerPrincipal, Sobre, Contato, PedidoOracao, CalendarioSemanal,
    Vocacional, CalendarioSemanalImagem, Baluartes,
    Socio, Casas)

from .forms import EmailForm, PedidoOracaoForm, SocioForm
from .utils import send_mail


class HomeView(FormView):
    template_name = 'home.html'
    form_class = EmailForm

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['banner'] = BannerPrincipal.objects.first()
        context['sobre'] = Sobre.objects.first()
        context['contato'] = Contato.objects.first()
        context['pedido_oracao'] = PedidoOracao.objects.first()
        context['baluartes'] = Baluartes.objects.all()
        context['vocacional'] = Vocacional.objects.first()
        context['socio'] = Socio.objects.first()
        context['imagem_calendario'] = CalendarioSemanalImagem.objects.first()
        context['eventos'] = Evento.objects.order_by('-data_inicio')[:6]
        context['fotos'] = Album.objects.order_by('-data')[:6]
        context['calendario_semanal'] = CalendarioSemanal.objects.all()
        context['casas'] = Casas.objects.all()
        today = datetime.now()
        lectio = LectioDivina.objects.filter(data=today)
        if lectio:
            context['lectio'] = lectio[0]

        return context

    def form_valid(self, form):
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        mensagem = '<br><strong>'+'Mensagem do Site'+'</strong>'+'<br>'+'Nome: '+form.cleaned_data['nome']+'<br>Email: '+form.cleaned_data['email']+'<br>Mensagem: '+form.cleaned_data['mensagem']

        send_mail(subject="Contato", body=nome, from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER], fail_silently=False, html=mensagem)
        return HttpResponseRedirect(reverse_lazy('home'))    

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class PedidoOracaoView(FormView):
    template_name = 'home.html'
    form_class = PedidoOracaoForm
    model = PedidosOracao

    def post(self, request):
        if (request.POST['nome'] and request.POST['email'] and request.POST['oracao'] and request.POST['estado'] and request.POST['cidade']):
            pedido = PedidosOracao.objects.create(nome=request.POST['nome'], email=request.POST['email'], oracao=request.POST['oracao'],
                        estado=request.POST['estado'], cidade=request.POST['cidade'])
            pedido.save()
            nome = request.POST['nome']
            email = request.POST['email']
            mensagem = PedidoOracao.objects.first().mensagem_resposta_automatica

            send_mail(subject="Pedido de Oração - Comunidade Verbo de Misericórdia", body=nome, from_email=settings.EMAIL_HOST_USER, recipient_list=[email], fail_silently=False, html=mensagem)
            messages.add_message(
            self.request, messages.SUCCESS, 'Pedido de oração salvo com sucesso!')
            return HttpResponseRedirect(reverse_lazy('home'))    
        else:
            messages.add_message(
            self.request, messages.ERROR, 'Não foi possível salvar o seu pedido de oração. Verifique se todos os campos foram preenchidos.')
            return form_invalid(self.form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SocioView(FormView):
    template_name = 'home.html'
    form_class = SocioForm
    model = Socio

    def post(self, request):
        if (request.POST['nome'] and request.POST['email']):
            nome = request.POST['nome']
            email = request.POST['email']
            mensagem = '<br><strong>'+'Mensagem do site - Novo sócio'+'</strong>'+'<br>'+'Nome: '+nome+'<br>Email: '+email+'<br>Mensagem: '+'Novo Sócio. Entrar em contato <br>:)'
            messages.add_message(
            self.request, messages.SUCCESS, 'Pedido de sócio enviado com sucesso. Aguarde que em breve entraremos em contato pelo e-mail.')
            send_mail(subject="Novo Sócio do site", body=nome, from_email=settings.EMAIL_HOST_USER, recipient_list=[settings.EMAIL_HOST_USER], fail_silently=False, html=mensagem)
            
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.add_message(
                self.request, messages.ERROR, 'Não foi possível salvar o seu pedido de oração. Verifique se todos os campos foram preenchidos.')
            return form_invalid(self.form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
