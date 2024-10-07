from django.db import models


class MyProfile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='folioapp/media/')
    biography = models.TextField(max_length=1000)

    def __str__(self):
        return self.first_name
    

class PorteFolio(models.Model):
    image = models.ImageField(upload_to='folioapp/media/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=150)


class Technology(models.Model):
    portefolio = models.ForeignKey(
        PorteFolio, 
        on_delete=models.CASCADE, 
        related_name='technologies',
    )
    image = models.ImageField(upload_to='folioapp/media/technologies/')


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField(max_length=1000)

