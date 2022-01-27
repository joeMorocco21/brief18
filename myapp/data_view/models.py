from django.db import models
from rest_framework import serializers
# Create your models here.
class data_view(models.Model):
    id_lot = models.TextField(null=True)
    nb_piece = models.IntegerField(null=True)
    typologie = models.TextField(null=True)
    prix_tva_reduite = models.FloatField(null=True)
    prix_tva_normale = models.FloatField(null=True)
    prix_ht = models.FloatField(null=True)
    prix_m2_ht = models.FloatField(null=True)
    prix_m2_ttc = models.FloatField(null=True)
    surface = models.FloatField(null=True)
    etage = models.IntegerField(null=True)
    orientation = models.TextField(null=True)
    exterieur = models.BooleanField(null=True)
    balcony = models.BooleanField(null=True)
    garden = models.BooleanField(null=True)
    parking = models.FloatField(null=True)
    nom_programme = models.TextField(null=True)
    ville = models.TextField(null=True)
    departement = models.FloatField(null=True)
    date_fin_programme = models.TextField(null=True)
    adresse_entiere = models.TextField(null=True)
    promoteur = models.TextField(null=True)
    date_extraction = models.TextField(null=True)
    index = models.IntegerField(null=True)
    
    def __str__(self):
        return self.ville