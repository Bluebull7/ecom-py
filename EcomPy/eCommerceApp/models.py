from django.db import models
from django.contrib.postgres.fields import ArrayField

# implement methods + logic in controller class for CRUD
# Create your models here.

#
class User(models.Model):
    _userId = models.IntegerField()
    _username = models.CharField(max_length=100)
    _email = models.CharField(max_length=255)
    _password = models.CharField(max_length=50)

  #  def __str__(self):
   #     return self.name
    

class Product(models.Model):
  #  _productID: ObjectId # undefined
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()


#    def __str__(self):
 #       return self.name
    

class Order(models.Model):
    _orderId = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE) # List of Type Product
    _Products = models.CharField(max_length=255)
    _totalAmount = models.FloatField() 
    _subtotal = models.FloatField()

class ShoppingCart(models.Model): 
    _user: User 
    _items = ArrayField(models.CharField(max_length=255)) 

class Category(models.Model): 
    categoryID = models.ForeignKey(ObjectId, on_delete=models.CASCADE) 
    name= models.CharField(max_length=255)


class orderItem (models.Model):

#    orderItemid: ObjectId = models.IntegerField()
 #   product: Product = models.CharField





    
