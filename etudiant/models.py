from django.db import models
class Etudiant(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    age=models.IntegerField()
    moyenne=models.FloatField()
    classe=models.CharField(max_length=50)
    dateInscription=models.DateField()

