from random import choices
from django.db import models

# Modelo de diagnostico de un usuario
# TODO: Falta realizar la relacion entre un user y el diagnostico

class Diagnostico(models.Model):
    LOW_WEIGHT = 'Bajo peso'
    NORMAL_WEIGHT = 'Peso normal'
    OVERWEIGHT = 'Sobrepeso'
    OBESITY = 'Obesidad'

    estadoPeso = [
        (LOW_WEIGHT, 'Bajo peso'),
        (NORMAL_WEIGHT, 'Peso normal'),
        (OVERWEIGHT, 'Sobrepeso'),
        (OBESITY, 'Obesidad'),
    ]

    fecha_diagnostico = models.DateField(auto_now_add=True, blank=True)
    estatura = models.FloatField(blank=False, null=False)
    peso = models.FloatField(blank=False, null=False)
    imc = models.FloatField(blank=True, null=False)
    estado = models.CharField(
        max_length=15, choices=estadoPeso, blank=True, null=False)

    # Funcion para calcular el imc
    def calc_imc(self):
        self.imc = self.peso / ((self.estatura)**2)

    # Funcion para comparar el IMC y asignar peso
    def compare_imc(self):
        if 0 <= self.imc < 18.5:
            self.estado = self.LOW_WEIGHT
        elif 18.5 <= self.imc <= 24.9:
            self.estado = self.NORMAL_WEIGHT
        elif 25.0 <= self.imc <= 29.9:
            self.estado = self.OVERWEIGHT
        else:
            self.estado = self.OBESITY

    def save(self, *args, **kwargs):

        # Se calcula el imc
        self.calc_imc()

        # Comparacion de pesos para asignar uno
        self.compare_imc()

        # Guardar nuevos datos en BD
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id']