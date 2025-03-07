from rest_framework import serializers
from usuario.models import Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ['username', 'email', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email= validated_data['email'],
            phone=validated_data['phone'],
            password=validated_data['password']
        )
        return user
    
    
class UsuarioInfoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ['username', 'email', 'phone']

