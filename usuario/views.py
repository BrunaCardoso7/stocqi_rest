from rest_framework import viewsets, status
from rest_framework.response import Response
from usuario.serializers import UsuarioInfoSerializer, UsuarioSerializer
from usuario.models import Usuario
from rest_framework.permissions import IsAuthenticated, AllowAny



# Create your views here.
class UsuarioView(viewsets.GenericViewSet):
    def get_serializer_class(self):
        if self.action == "signup":
            return UsuarioSerializer
        elif self.action == "retrieve":
            return UsuarioInfoSerializer
        elif self.action == "list":
            return UsuarioInfoSerializer
    def get_queryset(self):
        return Usuario.objects.all() 
    def get_permissions(self):
        if self.action == "signup":
            return [AllowAny()]  
        elif self.action == "list":
            return [IsAuthenticated()]  
        elif self.action == "retrieve":
            return [IsAuthenticated()]  
        return super().get_permissions()
    def signup (self, request):
        user_serializer = self.get_serializer(data=request.data)
        if user_serializer.is_valid():
            user = user_serializer.save()
            print(user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, id):
        try:
            user =  Usuario.objects.get(id=id)
            user_serializer = UsuarioSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response(
                {'msg': 'Usuário não encontrado!'},
                status=status.HTTP_404_NOT_FOUND
            )
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.get_serializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    