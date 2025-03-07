from django.urls import path
from produto.views import ProdutoViewSet

urlpatterns = [
    path(
        "create/", ProdutoViewSet.as_view(
            {
                'post': "create",
            }
        ), name='produto'
    )
]