from django.db import models

# Create your models here.
class Artisan(models.Model):
    nom=models.CharField(max_length=200,null=True)
    prenom=models.CharField(max_length=200,null=True)
    telephone=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom+" "+self.prenom

class Atelier(models.Model):
    nom=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    localisation=models.CharField(max_length=300,null=True)
    proprietaire=models.ForeignKey(Artisan,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='static/images/image_atelier',null=True)
