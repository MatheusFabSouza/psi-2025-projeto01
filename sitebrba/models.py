from django.db import models

class Elenco(models.Model):
    nome = models.CharField(max_length=200)
    idade_em_serie = models.IntegerField(null=True, blank=True)
    posicao = models.CharField(max_length=100, blank=True)
    nascimento = models.CharField(max_length=200, blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="sitebrba/img/", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Elenco"

