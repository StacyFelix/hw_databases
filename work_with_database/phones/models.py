from datetime import datetime

from django.db import models
from django.utils import timezone


class Phone(models.Model):

    id = models.PositiveIntegerField(
        primary_key=True,
        serialize=False
    )

    name = models.CharField(
        max_length=60
    )
    image = models.CharField(
        max_length=255
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    release_date = models.DateField(
        default=datetime.now().strftime("%Y-%m-%d")
    )

    slug = models.SlugField(
        unique=True
    )
