from django.db import models

# classe que cria os topicos que serao adicionados pelos usuarios durante a utilizacao do projeto
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

# retorna uma representacao em str do modelo
    def __str__(self):
        return self.text