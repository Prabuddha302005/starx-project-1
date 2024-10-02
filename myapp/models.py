from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()

class ServicePhotos(models.Model):
    category = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="servicesPhotos")


class OurServicesPhotos(models.Model):
    photo = models.ImageField(upload_to="ourServicesPhotos")
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)