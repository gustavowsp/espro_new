from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Vaga(models.Model):
  titulo_vaga     = models.CharField(max_length=25)
  descricao_vaga  = models.TextField()
  foto_vaga       = models.ImageField(upload_to='pictures',blank=True)
  salario_vaga    = models.FloatField()
  localidade_Vaga = models.CharField(max_length=60)
  owner = models.ForeignKey(
    User,on_delete=models.SET_NULL,
    blank=True,null=True
    )
  
  def __str__(self) -> str:
    return self.titulo_vaga