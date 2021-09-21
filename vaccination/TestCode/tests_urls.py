from django.test import SimpleTestCase
from django.urls import reverse,resolve
from vaccination.controller import registration, status, certification, vaccine_card
class TestUrls(SimpleTestCase):

    def test_registration_url_is_resolved(self):
        url = reverse('registration')
#        print(resolve(url))
        self.assertEquals(resolve(url).func, registration)
    
    def test_certification_url_is_resolved(self):
        url = reverse('certification')
        self.assertEquals(resolve(url).func, certification)

    def test_status_url_is_resolved(self):
        url = reverse('status')
        self.assertEquals(resolve(url).func, status)
    
    def test_vaccine_card_url_is_resolved(self):
        url = reverse('vaccine_card')
        self.assertEquals(resolve(url).func, vaccine_card)