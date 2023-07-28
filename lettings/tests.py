from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class LettingsTest(TestCase):

    def setUp(self):
        self.address = Address.objects.create(
            number=1,
            street="Rue du Test",
            city="Paris",
            state="Ile de France",
            zip_code=75001,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(title="Test Letting", address=self.address)

    def test_lettings_index(self):
        response = self.client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert b"<title>Lettings</title>" in response.content

    def test_letting_detail(self):
        response = self.client.get(reverse('lettings:letting', args=[1]))
        assert response.status_code == 200
        assert b"<title>Test Letting</title>" in response.content

    def test_address_model(self):
        assert str(self.address) == f'{self.address.number} {self.address.street}'


    def test_letting_model(self):
        assert str(self.letting) == self.letting.title