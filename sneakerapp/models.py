from django.core.validators import validate_comma_separated_integer_list
from django.db import models


# Create your models here.


SNEAKER_MODELS = [
        ("Nike", "Nike"),
        ("Adidas", "Adidas"),
        ("Reebok", "Reebok"),
        ("Puma", "Puma"),
        ("Converse", "Converse"),
    ]


SNEAKER_COLORS = [
        ("White", "White"),
        ("Black", "Black"),
        ("Red", "Red"),
        ("Gray", "Gray"),
        ("Light Blue", "Light Blue"),
    ]


SNEAKER_SIZES = [
    ("37", "37"),
    ("38", "38"),
    ("39", "39"),
    ("40", "40"),
    ("41", "41"),
    ("42", "42"),
    ("43", "43"),
    ("44", "44"),
    ("45", "45"),
    ("46", "46"),
]


class Sneaker(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50, choices=SNEAKER_MODELS)
    price = models.IntegerField()
    size = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    color = models.CharField(max_length=20, choices=SNEAKER_COLORS)

    def __str__(self):
        return self.name
