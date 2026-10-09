from django.db import models
from django.urls import reverse,reverse_lazy

fuels = [
    ('PETROL','Petrol'),
    ('DIESEL','Diesel'),
    ('EV','ev')
    ]

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    est_yer = models.IntegerField()
    origien = models.CharField(max_length=100)
    comp_logo = models.ImageField(upload_to='logos/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company_detail', kwargs={'pk': self.pk})

class Producets(models.Model):
    prod_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    color =models.CharField(max_length=100)
    engien_cc = models.CharField(max_length=100)
    fuel_Type = models.CharField(max_length=100,choices=fuels)
    miliege = models.CharField(max_length=100)
    settings =models.IntegerField()
    company = models.ForeignKey(Company,related_name="companies",on_delete=models.CASCADE)
    prod_image = models.ImageField(upload_to='productimage/', null=True, blank=True)

    def __str__(self):
            return self.prod_name

    def get_success_url(self):
        return reverse_lazy('company_detail',kwargs={'pk': self.object.company.pk})


class LoanApplication(models.Model):
    product = models.ForeignKey(Producets,related_name="application",on_delete=models.CASCADE)
    down_payment =models.DecimalField(max_digits=10,decimal_places=2)
    loan_amount = models.DecimalField(max_digits=10,decimal_places=2)
    tenure = models.IntegerField()
    interest_rate = models.FloatField()
    emi = models.DecimalField(max_digits=10,decimal_places=2)
    total_payment = models.DecimalField(max_digits=10,decimal_places=2)
    total_interest = models.DecimalField(max_digits=10,decimal_places=2)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f"{self.product.prod_name} - {self.tenure}yer - ₹{self.emi}/month"



