import pytest
from .models import Letting, Address


@pytest.fixture
def sample_address():
    """
    Create and return a sample address instance.

    Returns:
    Address: A sample address instance.
    """
    return Address.objects.create(
        number=123,
        street="Main Street",
        city="City",
        state="ST",
        zip_code=12345,
        country_iso_code="USA",
    )


@pytest.fixture
def sample_letting(sample_address):
    """
    Create and return a sample letting instance.

    Args:
    sample_address (Address): A sample address instance.

    Returns:
    Letting: A sample letting instance.
    """
    return Letting.objects.create(title="Test Letting", address=sample_address)


@pytest.fixture
def wrong_sample_letting():
    """
    Create and return a wrong sample letting instance.

    Returns:
    Letting: A wrong sample letting instance.
    """
    return Letting.objects.create(title="Test Letting", address=None)


@pytest.mark.django_db
def test_lettings_list_returns_200(client, sample_letting):
    """
    Test whether the lettings view returns a status code of 200
    for lettings listing and specific letting retrieval.

    Args:
    client: Django test client.
    sample_letting (Letting): A sample letting instance.

    Returns:
    None
    """
    response_1 = client.get("/lettings/")

    assert response_1.status_code == 200
    assert sample_letting.title.encode() in response_1.content


@pytest.mark.django_db
def test_lettings_instance_return_200(client, sample_letting):
    """
    Test whether the lettings view returns a status code of 200
    for specific letting retrieval.

    Args:
    client: Django test client.
    sample_letting (Letting): A sample letting instance.

    Returns:
    None
    """
    response = client.get(f"/lettings/{sample_letting.id}/")

    assert response.status_code == 200

    assert sample_letting.title.encode() in response.content
    assert sample_letting.address.street.encode() in response.content


@pytest.mark.django_db
def test_add_letting(sample_letting):
    """
    Test adding a letting.

    Args:
    sample_letting (Letting): A sample letting instance.

    Returns:
    None
    """
    # Verify that the addition was successful
    assert Letting.objects.count() == 1
    assert Letting.objects.first() == sample_letting


@pytest.mark.django_db
def test_update_letting(sample_letting):
    """
    Test updating a letting.

    Args:
    sample_letting (Letting): A sample letting instance.

    Returns:
    None
    """
    # Update the letting
    updated_title = "New Title"
    sample_letting.title = updated_title
    sample_letting.save()

    # Verify that the update was successful
    updated_letting = Letting.objects.get(id=sample_letting.id)
    assert updated_letting.title == updated_title


@pytest.mark.django_db
def test_delete_letting(sample_letting):
    """
    Test deleting a letting.

    Args:
    sample_letting (Letting): A sample letting instance.

    Returns:
    None
    """
    # Delete the letting
    sample_letting.delete()

    # Verify that the deletion was successful
    assert Letting.objects.count() == 0


@pytest.mark.django_db
def test_update_address(sample_address):
    """
    Test updating an address.

    Args:
    sample_address (Address): A sample address instance.

    Returns:
    None
    """
    # Update the address
    updated_street = "New Street"
    sample_address.street = updated_street
    sample_address.save()

    # Verify that the update was successful
    updated_address = Address.objects.get(id=sample_address.id)
    assert updated_address.street == updated_street


@pytest.mark.django_db
def test_delete_address(sample_address):
    """
    Test deleting an address.

    Args:
    sample_address (Address): A sample address instance.

    Returns:
    None
    """
    # Delete the address
    sample_address.delete()

    # Verify that the deletion was successful
    assert Address.objects.count() == 0
