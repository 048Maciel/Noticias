from django.db import models
from django.urls import reverse

class Artigo(models.Model):
    titulo = models.CharField(max_length=200)
    corpo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_publicacao']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('artigo_detail', args=[str(self.id)])

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentário em {self.artigo.titulo[:30]}'