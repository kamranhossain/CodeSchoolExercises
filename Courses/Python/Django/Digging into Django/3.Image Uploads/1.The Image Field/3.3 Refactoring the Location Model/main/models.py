from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100)
    num_restaurants = models.IntegerField()
    predators = models.CharField(max_length=100)
    img = models.ImageField(upload_to='location_images',
                            default='location_images/default.png')

    def __str__(self):
        return self.name
