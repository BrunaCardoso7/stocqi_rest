from rest_framework import serializers
from produto.models import Produto


class CreateProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto
        fields = [
            'id',  
            'nome',
            'descricao',
            'beneficios',
            'modo_de_uso',
            'especificacao',
            'indicacao',
            'garatia_de_qualidade',
            'preco_estimado',
            'preco',
            'user',
        ]

    def create(self, validated_data):
        return Produto.objects.create(**validated_data)
    
class ListProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto   
        fields = "__all__"  
        
class ListByIdProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto   
        fields = "__all__"
    
class UpdateByIdProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto   
        fields = "__all__"
        
class DeleteByIdProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Produto   
        fields = "__all__"
