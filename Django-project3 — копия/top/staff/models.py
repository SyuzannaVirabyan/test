from django.db import models

# Create your models here.
class CancelRequst(models.Model):
    order = models.ForeignKey('store.Order', on_delete=models.CASCADE)