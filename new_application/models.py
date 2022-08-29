from django.db import models
import random

class User(models.Model):
    # pk
    # Next : Dynamic input from prospective clients :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    unique_card_num = models.CharField(default='6054')
    routing_num = models.CharField(default=str(random.randint(1000, 9999)))
    account_num = models.CharField(default=str(random.randint(100000, 999999)))

    def __str__(self):
        return f'Client {self.first_name} {self.last_name}'