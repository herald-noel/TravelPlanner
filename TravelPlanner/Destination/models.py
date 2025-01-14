from django.db import models
from django.utils import timezone

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    contact_number = models.CharField(max_length=11)
    balance = models.FloatField()

    def __str__(self):
        return self.username


class Destinations(models.Model):
    destination_id = models.BigAutoField(primary_key=True)
    destination_name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=20)

    def __str__(self):
        return self.destination_name


class Review(models.Model):
    review_id = models.BigAutoField(primary_key=True)
    destination = models.ForeignKey(Destinations, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.review_id
