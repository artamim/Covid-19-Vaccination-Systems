from django.db import models

# Create your models here.
class vaccination(models.Model):
    NID_Number = models.IntegerField()
    Birth_Date = models.DateField()
    Phone=models.IntegerField()
    Service=models.CharField(max_length=30)
    Extra_Info=models.CharField(max_length=30 ,blank=True)
    Status=models.BooleanField(default=False)
    Certificate_Img=models.ImageField(upload_to='pics', blank=True)
    Certificate_Status=models.BooleanField(default=False)
    VaccineCard_Img=models.ImageField(upload_to='pics2', blank=True)
    VaccineCard_Status=models.BooleanField(default=False)