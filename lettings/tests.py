import pytest
from django.test import RequestFactory
from .models import Letting, Address
from .views import index, lettings_index, letting

@pytest.fixture
def lettings():
    # Create sample Address and Letting instances for testing
    address = Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="TST"
    )
    letting = Letting.objects.create(title="Test Letting", address=address)
    return [letting]

@pytest.mark.django_db
def test_index_view():
    factory = RequestFactory()
    request = factory.get("/")
    response = index(request)
    assert response.status_code == 200
    assert "index.html" in response.template_name

@pytest.mark.django_db
def test_lettings_index_view(lettings):
    factory = RequestFactory()
    request = factory.get("/lettings/")
    response = lettings_index(request)
    assert response.status_code == 200
    assert "lettings_index.html" in response.template_name
    assert "lettings_list" in response.context

@pytest.mark.django_db
def test_letting_view(lettings):
    letting = lettings[0]
    factory = RequestFactory()
    request = factory.get(f"/lettings/{letting.id}/")
    response = letting(request, letting_id=letting.id)
    assert response.status_code == 200
    assert "letting.html" in response.template_name
    assert "title" in response.context
    assert "address" in response.context
