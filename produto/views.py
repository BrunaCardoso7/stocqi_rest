from rest_framework import viewsets, status
from produto.models import Produto
from produto.serializers import CreateProdutoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = CreateProdutoSerializer
    queryset = Produto.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self, request):
        """
        Purpose: Registra um novo produto
        """
        produto_serializer = self.get_serializer(data=request.data)
        if produto_serializer.is_valid():
            produto = produto_serializer.save()
            print(produto)
            return Response(produto_serializer.data, status=status.HTTP_201_CREATED)
        return Response(produto_serializer.errors, status=status.HTTP_200_OK)