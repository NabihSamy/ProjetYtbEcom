from django.db import models

# Create your models here.

"""
Produit : 
    - Titre
    - Description
    - Prix
    - Image
Client : 
    - Nom
    - Prénom
    - Email
Vendeur : 
    - Nom
    - Prénom
    - Email
Commande :
    - Client
    - Produit
    - Quantité
    - Date
    - Vendeur
"""
class Product(models.Model):
    title =         models.CharField(max_length=120)
    price =         models.FloatField(default=0.0)
    stock =         models.IntegerField(default=0)
    description =   models.TextField(blank=True)
    Image =         models.ImageField(upload_to='products/', blank=True, null=True)

