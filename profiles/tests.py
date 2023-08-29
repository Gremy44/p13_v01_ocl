import pytest
import uuid
from django.contrib.auth.models import User
from .models import Profile


@pytest.fixture(scope="function")
def sample_user():
    """
    Create a sample user object with a unique username.

    Returns:
    User: A sample user instance.
    """
    unique_username = f"testuser_{uuid.uuid4().hex[:10]}"
    return User.objects.create_user(username=unique_username, password="testpassword")


@pytest.fixture(scope="function")
def sample_profile(sample_user):
    """
    Create a sample profile object associated with the sample user.

    Args:
    sample_user (User): A sample user instance.

    Returns:
    Profile: A sample profile instance.
    """
    return Profile.objects.create(user=sample_user, favorite_city="Test City")


@pytest.mark.django_db
def test_profiles_returns_200(client, sample_profile):
    """
    Test whether the profiles view returns a status code of
    200 for profile listing and specific profile retrieval.

    Args:
    client: Django test client.
    sample_profile (Profile): A sample profile instance.

    Returns:
    None
    """
    # Perform GET request to retrieve profile list
    response_1 = client.get("/profiles/")
    assert response_1.status_code == 200


@pytest.mark.django_db
def test_profiles_instance_return_200(client, sample_profile):
    """
    Test whether the profiles view returns a status code of
    200 for specific profile retrieval.

    Args:
    client: Django test client.
    sample_profile (Profile): A sample profile instance.

    Returns:
    None
    """
    profile_test = Profile.objects.first()

    # Perform GET request to retrieve specific user profile
    response = client.get(f"/profiles/{profile_test}/")

    assert response.status_code == 200
    assert profile_test.favorite_city.encode() in response.content


@pytest.mark.django_db
def test_add_profile(sample_user, sample_profile):
    """
    Test adding a user profile.

    Args:
    sample_user (User): A sample user instance.
    sample_profile (Profile): A sample profile instance.

    Returns:
    None
    """
    profile_test = Profile.objects.first()

    # Verify that the addition was successful
    assert Profile.objects.count() == 1
    assert Profile.objects.first() == profile_test


@pytest.mark.django_db
def test_update_profile(sample_user, sample_profile):
    """
    Test updating a user profile.

    Args:
    sample_user (User): A sample user instance.
    sample_profile (Profile): A sample profile instance.

    Returns:
    None
    """
    profile_test = Profile.objects.first()
    user_test = User.objects.first()

    # Update the profile
    updated_city = "New City"
    profile_test.favorite_city = updated_city
    profile_test.save()

    # Verify that the update was successful
    updated_profile = Profile.objects.get(user=user_test)
    assert updated_profile.favorite_city == updated_city


@pytest.mark.django_db
def test_delete_profile(sample_profile):
    """
    Test deleting a user profile.

    Args:
    sample_profile (Profile): A sample profile instance.

    Returns:
    None
    """
    profile_test = Profile.objects.first()

    # Delete the profile
    profile_test.delete()

    # Verify that the deletion was successful
    assert Profile.objects.count() == 0
