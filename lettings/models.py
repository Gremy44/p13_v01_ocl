from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    Attributes:
    - number (PositiveIntegerField): The street number.
    - street (CharField): The street name.
    - city (CharField): The city name.
    - state (CharField): The state abbreviation (2 characters).
    - zip_code (PositiveIntegerField): The ZIP code.
    - country_iso_code (CharField): The ISO country code (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        return f"{self.number} {self.street}"

    class Meta:
        db_table = "lettings_address"

        # modify the plural name of the model in the admin interface
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Model representing a letting property.

    Attributes:
    - title (CharField): The title of the letting.
    - address (OneToOneField): The associated address of the letting.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "lettings_letting"
