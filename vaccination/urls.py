from django.urls import path
from . import controller
urlpatterns = [
    path('registration', controller.registration, name="registration"),
    path('certification', controller.certification, name="certification"),
    path('status', controller.status, name="status"),
    path('vaccine_card', controller.vaccine_card, name="vaccine_card")
]