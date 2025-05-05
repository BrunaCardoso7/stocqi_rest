from django.urls import path
from .views import UsuarioView

urlpatterns = [
    path("auth/", UsuarioView.as_view(
        {
            'post': 'signup',
        }
    ), name="user"),
    path("user/", UsuarioView.as_view(
        {
            'get': 'list'
        }
    ), name="user-list"),
    path("user/<int:id>/", UsuarioView.as_view(
        {
            'get': 'retrieve'
        }
    ), name="user-detail")
]