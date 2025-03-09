from django.urls import path
from produto.views import ProdutoViewSet
from avaliacao.views import AvaliacaoViewSet

urlpatterns = [
    path(
        "create/", ProdutoViewSet.as_view(
            {
                'post': "create",
            }
        ), name='produto'
    ),
    path(
        "list/<uuid:pk>/", ProdutoViewSet.as_view(
            {
                'get': "retrieve",
            }
        ), name='produto-detail'
    ),
    path(
        "list/", ProdutoViewSet.as_view(
            {
                'get': "list",
            }
        ), name='produto-list'
    ),
    path('<uuid:produto_id>/avaliacoes/', AvaliacaoViewSet.as_view({'get': 'list', 'post': 'create'}), name='avaliacoes-produto'),
    path('<uuid:produto_id>/avaliacoes/<uuid:pk>/', AvaliacaoViewSet.as_view({'get': 'retrieve'}), name='avaliacao-detail'),
]