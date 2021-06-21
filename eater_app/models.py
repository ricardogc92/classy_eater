from django.db import models
from django.db.models.deletion import CASCADE
from login_app.models import User
# Create your models here.

class RestaurantManager(models.Manager):
    def validator(self, post_data):
        errors={}
        if len(post_data['name'])<2:
            errors['name']= "Restaurant name has to be at least 2 characters"
        if post_data['category']=="Food Category":
            errors['category']="Please choose a category of food"
        if len(post_data['city'])<1:
            errors['city']="City cannot be left empty"
        if len(post_data['city'])<1:
            errors['zip_code']="Zip Code cannot be left empty"
        if len(post_data['capacity'])<1:
            errors['capacity']="Capacity needs to be greater than 0"
        return errors

class ReservationManager(models.Manager):
    def validator(self,post_data):
        errors={}
        restaurant=Restaurant.objects.get(id=post_data['res_id'])
        

class Restaurant(models.Model):
    name=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    zip_code=models.CharField(max_length=15)
    capacity=models.IntegerField()
    image=models.ImageField(upload_to='images/')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User, related_name="restaurants_owned", on_delete=models.CASCADE)
    user_reservations=models.ManyToManyField(User,related_name='restaurant_reservations', through='Reservation')
    objects=RestaurantManager()


class Reservation(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    guests=models.CharField(max_length=40)
    date=models.DateField()
    time=models.TimeField()
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    objects=ReservationManager()



