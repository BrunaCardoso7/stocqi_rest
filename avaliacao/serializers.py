from rest_framework import serializers
from avaliacao.models import Avaliacao

class CreateAvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avaliacao
        fields = '__all__'
    def create(self, validated_data):
        return Avaliacao.objects.create(**validated_data)
    
class RetriveAvaliacaoSerializer(serializers.ModelSerializer):
    user_id = serializers.StringRelatedField()
    product_id = serializers.StringRelatedField()
    class Meta:
        model=Avaliacao
        fields = '__all__'
        
class RetriveByIdAvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Avaliacao
        fields = '__all__'
