from django.urls import path
from avaliacao.views import AvaliacaoViewSet

urlpatterns=[
    path('create/',
            AvaliacaoViewSet.as_view(
                { 
                    'post': 'create',
                }
            )
        ),
    path('<uuid:id>/',
            AvaliacaoViewSet.as_view(
                { 
                    'get': 'retrieve',
                }
            )
        )
]