from django.db import models
import uuid

# Create your models here.
class Avaliacao(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False),
    user_id = models.ForeignKey('usuario.Usuario', on_delete=models.SET_NULL, null=False, related_name="avaliar"),
    produto_id = models.ForeignKey('produto.Produto', on_delete=models.SET_NULL, null=False, related_name="produtoavaliado"),
    nota = models.DecimalField(max_digits=1, decimal_places=0)
    comentario = models.TextField(null=True, blank=True)