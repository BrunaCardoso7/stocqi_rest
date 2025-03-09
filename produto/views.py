from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from produto.models import Produto
from produto.serializers import CreateProdutoSerializer, ListProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProdutoSerializer
        elif self.action == 'retrieve':
            return ListProdutoSerializer
        elif self.action == 'list':
            return ListProdutoSerializer
        return ListProdutoSerializer  
    
    def get_queryset(self):
        produto_id = self.kwargs.get('produto_id')
        if produto_id:
            return Produto.objects.filter(produto_id=produto_id)
        return Produto.objects.all()
    def get_permissions(self):
            if self.action == "create":
                return [IsAuthenticated()]  
            elif self.action == "list":
                return [AllowAny()]  
            elif self.action == "retrieve":
                return [AllowAny()]  
            return super().get_permissions()

    def create(self, request, *args, **kwargs):
        """
        Purpose: Registra um novo produto
        """
        request.data['user'] = request.user.id 
        produto_serializer = self.get_serializer(data=request.data)
        if produto_serializer.is_valid():
            produto_serializer.save()
            return Response(produto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(produto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        try:
            produtos = self.get_queryset()
            serializer = self.get_serializer(produtos, many=True) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Produto.DoesNotExist:
            return Response({'msg': 'Nenhum produto encontrado!'}, status=status.HTTP_404_NOT_FOUND)
        
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'msg': 'Nenhum produto encontrado!'}, status=status.HTTP_404_NOT_FOUND)