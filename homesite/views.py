from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages


from django.shortcuts import render

from django.views.generic import TemplateView, FormView

from agenda.models import Evento
from pedidos_oracao.models import PedidosOracao

from .models import (
    BannerPrincipal, Sobre, Contato, PedidoOracao, CalendarioSemanal)

from .forms import EmailForm, PedidoOracaoForm
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
        context['eventos'] = Evento.objects.order_by('-data_inicio')[:6]
        context['calendario_semanal'] = CalendarioSemanal.objects.all()
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