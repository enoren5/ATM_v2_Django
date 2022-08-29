from django.db import models
import random
import datetime
from django.utils.timezone import now

class User(models.Model):
    
    # pk
    
    # Next : Dynamic input from prospective clients :
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    year_of_birth = models.CharField(max_length=4,default='1900')
    
    # Unique data generated for each new client after approval :
    application_approval_date = models.DateField(auto_now_add=False, default=now)
    unique_card_num = models.CharField(max_length=4, default='6054')
    routing_num = models.CharField(max_length=5, default=str(random.randint(10000, 99999)))
    account_num = models.CharField(max_length=7, default=str(random.randint(1000000, 9999999)))

    def __str__(self):
        return f'Client {self.first_name} {self.last_name}'