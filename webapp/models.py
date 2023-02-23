from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Car(models.Model):
    """Car model"""
    TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]
    title = models.CharField(max_length=100)
    door_num = models.PositiveIntegerField()
    seat_num = models.PositiveIntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    rating = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5),
    ])
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='car_photos/', blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title