from django.db import models

# Create your models here.
class Chapa(models.Model):
    
    usuario = models.OneToOneField(
        'myapp.Usuario',
        verbose_name='Usuario',
        on_delete=models.PROTECT,
    )
    
    nome = models.CharField(
        verbose_name='Nome:',
        max_length=255, null=False, blank=False,
    )
    
    cpf = models.CharField(
        verbose_name='CPF:',
        max_length=11,
        unique=True
    )
    
    cel = models.CharField(
        verbose_name='Cel: (11) 93759-8432',
        max_length=11,
    )
    
    data_nascimento = models.DateField(
        verbose_name='Data de nacimento',
        auto_now=False,
        auto_now_add=False,
        max_length=50,
    )
    
    class Meta:
        verbose_name = 'Porteiro'
        verbose_name_plural = 'Porteiros'
        db_table = 'porteiro'
        
    def __str__(self):
        return self.nome
    