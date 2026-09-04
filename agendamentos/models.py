from django.db import models
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    def __str__(self):
        return self.nome

class Pet(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=100)
    idade = models.IntegerField()
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
class Veterinario(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.nome
class Agendamentos(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()

    class Meta:
                  verbose_name_plural = 'Agendamentos' 
                  constraints =  [ models.UniqueConstraint(fields=['veterinario', 'data', 'horario'],
    name = 'agendamento_unico_por_veterinario'
    )
                  ]
def __str__(self):
        return f'{self.pet.nome} - {self.data} as {self.horario}'