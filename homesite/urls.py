from django.conf.urls import url

from .views import HomeView, PedidoOracaoView

urlpatterns = [
    url(r'^$',
        HomeView.as_view(), name='home'),
    url(r'^pedido/$',
        PedidoOracaoView.as_view(), name='pedido_oracao'),
]
