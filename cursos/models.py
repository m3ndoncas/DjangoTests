from django.db import models

class Poduto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=30)
    sobrenome = models.CharField('sobrenome', max_length=30)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'