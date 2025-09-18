from django.db import models

class Elenco(models.Model):
    # Removemos o id explícito; o Django criará automaticamente um id IntegerField PK.
    nome = models.CharField(max_length=50)
    idade_em_serie = models.CharField(max_length=2, blank=True)
    personagem = models.CharField(max_length=50, blank=True)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="elenco/", null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Elenco"


class Sobre(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    autor = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name_plural = "Sobre"
