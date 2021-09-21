from django.test import TestCase, Client
from django.urls import reverse
from vaccination.models import vaccination
import json
class TestController(TestCase):
    def setUp(self):
        self.client= Client()
        self.registration_url=reverse('registration')
        self.status_url=reverse('status')
        self.certification_url=reverse('certification')
        self.vaccine_card_url=reverse('vaccine_card')


    def test_registration_GET(self):
        
        response=self.client.get(self.registration_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'registration.html')

    def test_status_GET(self):
        
        response=self.client.get(self.status_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'status.html')

    def test_certification_GET(self):
        
        response=self.client.get(self.certification_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'certification.html')
    
    def test_vaccine_card_GET(self):
        
        response=self.client.get(self.vaccine_card_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'vaccine_card.html')


    def test_registration_POST(self):
        response=self.client.post( self.registration_url,
            {
                'nid': 121,
                'date': '2021-09-16',
                'phone': 1212,
            #    'service': 'Student 18 years or older',
                'service':'Military and paramilitary defence forces',
                'extra1': 'navy',
            }
        )

        self.assertEquals(response.status_code,302)
        self.assertEquals(vaccination.objects.first().NID_Number,121)


    def test_status_POST(self):
        vaccine1=vaccination.objects.create(
            NID_Number= 121,
            Birth_Date='2021-09-16',
            Phone=1212,
#            Status=1
        )
        response=self.client.post( self.status_url,
            {
                'nid':121,
                'date':'2021-09-16',
                'phone':1212,
            }
        )
        self.assertEquals(response.status_code,302)

    def test_certification_POST(self):
        vaccine1=vaccination.objects.create(
            NID_Number= 121,
            Birth_Date='2021-09-16',
            Phone=1212,
            #select both & (Use render) for positive value
            Certificate_Status=1, 
            Certificate_Img='pics/Screenshot_33.png'
        )
        response=self.client.post( self.certification_url,
            {
                'nid':121,
                'date':'2021-09-16',
                'phone':1212,
            }
        )
        #for rendering or redirecting (one or the other)
        self.assertEquals(response.status_code,200)  #render
    #    self.assertEquals(response.status_code,302)  #redirect

    def test_vaccine_card_POST(self):
        vaccine1=vaccination.objects.create(
            NID_Number= 121,
            Birth_Date='2021-09-16',
            Phone=1212,
            #select both & (Use render) for positive value
    #        VaccineCard_Status=1,
    #        VaccineCard_Img='pics/Screenshot_33.png'
        )
        response=self.client.post( self.vaccine_card_url,
            {
                'nid':121,
                'date':'2021-09-16',
                'phone':1212,
            }
        )
        #for rendering or redirecting (one or the other)
    #    self.assertEquals(response.status_code,200)  #render
        self.assertEquals(response.status_code,302)  #redirect
    