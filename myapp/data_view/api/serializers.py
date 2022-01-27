from rest_framework import serializers
# Create your models here.
class DataSerializers(serializers.Serializer):
    id_lot = serializers.CharField()
    nb_piece = serializers.IntegerField()
    typologie = serializers.CharField()
    prix_tva_reduite = serializers.FloatField()
    prix_tva_normale = serializers.FloatField()
    prix_ht = serializers.FloatField()
    prix_m2_ht = serializers.FloatField()
    prix_m2_ttc = serializers.FloatField()
    surface = serializers.FloatField()
    etage = serializers.IntegerField()
    orientation = serializers.CharField()
    exterieur = serializers.BooleanField()
    balcony = serializers.BooleanField()
    garden = serializers.BooleanField()
    parking = serializers.FloatField()
    nom_programme = serializers.CharField()
    ville = serializers.CharField()
    departement = serializers.FloatField()
    date_fin_programme = serializers.CharField()
    adresse_entiere = serializers.CharField()
    promoteur = serializers.CharField()
    date_extraction = serializers.CharField()
    index = serializers.IntegerField()
