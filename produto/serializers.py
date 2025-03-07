from rest_framework import serializers
from produto.models import Produto


class CreateProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto
        fields = '__all__'
    def create(self, validated_data):
        return Produto.objects.create(**validated_data)
    
    # end def
class ListProdutoSerializer:
    model=Produto   
    fields = "__all__"  
class ListByIdProdutoSerializer:
    model=Produto   
    fields = "__all__"
class UpdateByIdProdutoSerializer:
    model=Produto   
    fields = "__all__"
class DeleteByIdProdutoSerializer:
    model=Produto   
    fields = "__all__"
