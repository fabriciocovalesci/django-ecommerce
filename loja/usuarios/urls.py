from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views as v

urlpatterns = [
    path('', v.home, name='home'),
    path('produtos/new/', v.cadastrar_produto, name='cadastro_produtos'),
    path('produtos/', v.produtos, name='produtos'),
    path('produtos/<int:pk>/', v.produtos_detalhe, name='produtos_detalhe'),
    path('produtos/<int:pk>/compra/', v.compra_produto, name='compra_produto'),
    path('produtos/<int:pk>/finalizando/', v.finalizando_compra, name='finalizando_compra'),
    path('produtos/add_carrinho/', v.add_carrinho),
    path('produtos/<int:pk>/edit/', v.produto_editar, name='produto_editar'),
    path('register/', v.Login.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

