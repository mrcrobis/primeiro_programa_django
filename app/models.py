from django.db import models

# classe que cria os topicos que serao adicionados pelos usuarios durante a utilizacao do projeto
class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

# retorna uma representacao em str do modelo para ser possivel identificar o que é (remove a criptografia)
    def __str__(self):
        return self.text
    
# classe que cria a anotação de dentro do topico
class Entry(models.Model):
    # link essa entry com o topic atraves da foreignkey, on_delete é obrigatório passar
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # mudar o plural, sem isso o django apenas adiciona S no final da class transformando de entrys nesse caso
    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            return self.text[:50] + '...'