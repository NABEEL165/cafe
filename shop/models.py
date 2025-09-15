from django.db import models



class contactus(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()

def __str__(self):
    return self.name




class TableBooking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"
    



class Specialty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='specialties/')



class menu(models.Model):
    name= models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menus/')


