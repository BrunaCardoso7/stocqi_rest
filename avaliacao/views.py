from rest_framework import viewsets, status
from avaliacao.serializers import (CreateAvaliacaoSerializer, RetriveAvaliacaoSerializer,
    RetriveByIdAvaliacaoSerializer)
from avaliacao.models import Avaliacao
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class AvaliacaoViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateAvaliacaoSerializer
        elif self.action ==  'retrieve':
            return RetriveByIdAvaliacaoSerializer
        elif self.action == 'list':
            return RetriveAvaliacaoSerializer
        
    def get_queryset(self):
        produto_id = self.kwargs.get('produto_id')
        if produto_id:
            return Avaliacao.objects.filter(produto_id=produto_id)
        return Avaliacao.objects.all()
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        produto_id= self.kwargs.get('produto_id')
        
        request.data['produto_id'] = produto_id
        
        avaliacao_serializer = self.get_serializer(data=request.data)
        if avaliacao_serializer.is_valid():
            avaliacao_serializer.save()
            return Response(avaliacao_serializer.data, status=status.HTTP_201_CREATED)
        return Response(avaliacao_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Avaliacao.DoesNotExist:
            Response({'msg:', 'Nenhuma avaliação registrada!'}, status=status.HTTP_404_NOT_FOUND)