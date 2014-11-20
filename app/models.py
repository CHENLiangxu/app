from django.db import models

# Create your models here.
class Lower(models.Model):
    nom = models.CharField(max_length=30)
    pernom = models.CharField(max_length=30)
    telephone_protable = models.CharField(max_length=16)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    
class Client(models.Model):
    nom = models.CharField(max_length=30)
    pernom = models.CharField(max_length=30)
    telephone_fix = models.CharField(max_length=16)
    telephone_protable = models.CharField(max_length=16)
    adress = models.CharField(max_length=200)
    pays = models.CharField(max_length=30)
    ville = models.CharField(max_length=50)
    code_postal = models.CharField(max_length=10)
    # civilite : 0 monsieur; 1 madame 2 mademoiselle; 
    civilite = models.IntegerField()
    date_naissance = models.DateField()
    date_rdv = models.DateTimeField()
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    #client -> avocat
    my_lower = models.ForeignKey(Lower)