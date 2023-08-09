from django.contrib import admin
from vagas.models import Vaga
# Register your models here.



@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
  ...