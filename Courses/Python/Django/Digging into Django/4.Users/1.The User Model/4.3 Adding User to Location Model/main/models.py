from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    num_restaurants = models.IntegerField()
    predators = models.CharField(max_length=100)
    img = models.ImageField(upload_to='location_images',
                            default='location_images/default.png')

    def __str__(self):
        return self.name 
