from django.conf.urls import url

from .views import HomeView, PedidoOracaoView, SocioView

urlpatterns = [
    url(r'^$',
        HomeView.as_view(), name='home'),
    url(r'^pedido/$',
        PedidoOracaoView.as_view(), name='pedido_oracao'),
    url(r'^socio/$',
        SocioView.as_view(), name='socio'),
]
