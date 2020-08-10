from django.db import models
from zipairlines.my_formula import *
import datetime

# Create your models here.
class Airplane(models.Model):
    uid = models.IntegerField()
    model_name = models.CharField(max_length=200)
    passenger_capacity= models.IntegerField()
    #calculated fields
    fueltank_cap = models.FloatField()
    consumption_per_minute =models.FloatField()
    max_minutes = models.TimeField()
    def _str(self):
        return self.model_name

    
    def get_model_name(self):
        return generate_model_number()
    
    @property
    def get_fueltank_cap(self):
        return fuel_cap(self.uid)
    
    @property
    def get_consumption_per_minute(self): # get consumption per minute via formula module
        return fuel_consumption(self.uid)
    
    @property
    def get_max_minutes(self): #get max minutes via formula module
        return maximum_minutes(self.uid, self.fueltank_cap,self.passenger_capacity)
    
    #save calculated fieldsc
    def save(self, *args, **kwargs):
        self.model_name = self.get_model_name
        self.fueltank_cap =self.get_fueltank_cap
        self.max_minutes = self.get_max_minutes
        self.consumption_per_minute = self.get_consumption_per_minute
        super(Airplane,self).save(*args, **kwargs)
    