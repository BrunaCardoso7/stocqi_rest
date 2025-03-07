from django.db import models
import uuid
from avaliacao.models import Avaliacao

# Create your models here.
class Produto(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        id_avaliacao = models.ForeignKey('avaliacao.Avaliacao', on_delete=models.SET_NULL, null=True,  blank=True, related_name="avaliacoes")
        nome = models.CharField(null=False, max_length=255)
        descricao = models.TextField(null=False)
        beneficios = models.JSONField(default=list)
        modo_de_uso = models.JSONField(default=list)
        especificacao = models.JSONField(default=list)
        indicacao = models.JSONField(default=list)
        garatia_de_qualidade = models.TextField(null=False)
        preco_estimado =  models.DecimalField(max_digits=10, decimal_places=2)
        preco = models.DecimalField(max_digits=10, decimal_places=2)
