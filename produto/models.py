from django.db import models
from django.utils import timezone
# Create your models here.
class Produto(models.Model):
        nm_produto = models.CharField(null=True, max_length=255)
        ds_produto = models.TextField(null=True)
        qtd_produto = models.IntegerField(null=True)
        qtd_min_produto = models.IntegerField(null=True, blank=True)
        vl_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
        dt_create = models.DateTimeField(auto_now_add=True)
        dt_update =  models.DateTimeField(auto_now=True)
        dt_deletado = models.DateTimeField(null=True, blank=True)
        class Meta:
                db_table = 'produtos'
                verbose_name = 'Produto'
                verbose_name_plural = 'Produtos'