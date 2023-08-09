from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Model representing a user profile.

    Attributes:
    - user (OneToOneField): The related user instance.
    - favorite_city (CharField): The user's favorite city.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="lettings_profile"
    )
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "profiles_profile"
