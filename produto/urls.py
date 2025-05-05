from django.urls import path
from produto.views import ProdutoViewSet

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
]