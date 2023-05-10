from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Order(models.Model):
    table = models.CharField(max_length=10)
    order = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer}"
    
    def get_absolute_url(self):
        return reverse('order-detail', kwargs={'pk': self.pk})