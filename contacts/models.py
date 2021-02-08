from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name  = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    company = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

    