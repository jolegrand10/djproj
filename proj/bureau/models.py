from django.db import models

# Create your models here.
class Bureau(models.Model):
    numero = models.IntegerField()
    batiment = models.CharField(max_length=1)

    class Meta:
        ordering=['batiment', 'numero']
        verbose_name = "Bureau"
        verbose_name_plural = "Bureaux"

    def __str__(self):
         return self.batiment+str(self.numero)


class Person(models.Model):
    prenom = models.CharField(max_length=50)
    bureau = models.ForeignKey(Bureau,
        on_delete=models.PROTECT,
    )
    class Meta:
        ordering=['prenom']
        verbose_name = "Personne"
        verbose_name_plural = "Personnes"


    def __str__(self):
         return self.prenom



