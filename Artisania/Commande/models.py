from django.db import models

# Create your models here.
from artisan_app.models import Artisan

from article_app.models import Article


class Commande(models.Model):
    STATUS=(('en instance','en instance'),
            ('non livré','non livré'),
            ('livré','livré'))
    client=models.ForeignKey(Artisan,null=True,on_delete=models.CASCADE)
    produit=models.ForeignKey(Article,null=True,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    data_created=models.DateTimeField(auto_now_add=True)
