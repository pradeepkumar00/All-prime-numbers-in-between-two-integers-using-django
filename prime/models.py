from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

class Prime(models.Model):
    prime_id = models.AutoField
    prime_f = models.CharField(max_length=500000000)
    prime_s = models.CharField(max_length=500000000)
    times = models.CharField(max_length=500)
    timelaps = models.CharField(max_length=500)
    totalprime = models.CharField(max_length=500000000000000000000000)