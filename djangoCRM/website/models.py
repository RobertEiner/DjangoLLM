from django.db import models



# Create your models here.
# models.Model: the base class provided by django for creating database models.
# Django will take this model and every time we create a record it will convert the python code to SQL
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) # create timestamp when the reord is created
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last name', max_length=50)
    address = models.CharField('Adress', max_length=50)
    city = models.CharField('City', max_length=50)

    # this method works like toString()
    def __str__(self):
        return(f"{self.first_name} {self.last_name}") #the f"{...}" is like a template string and lets you embed variables in the string
    
class Item(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField('Category', max_length=50)
    price = models.CharField('Price', max_length=7)
    name = models.CharField('Name', max_length=50)
    color = models.CharField('Color', max_length=20)
    image = models.ImageField(null=True, blank=True, upload_to='images/') # the image goes to the media directory

    def __str__(self):
        return(f"{self.name}")
    
