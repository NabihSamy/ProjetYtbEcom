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
    name =         models.CharField(max_length=120)
    slug =          models.SlugField(max_length=120, default="") 
    price =         models.FloatField(default=0.0)
    stock =         models.IntegerField(default=0)
    description =   models.TextField(blank=True)
    thumbnail =     models.ImageField(upload_to="products", blank=True, null=True)

    def __str__(self):
        return self.title