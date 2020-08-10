from django.db import models
from airlines.my_computations import *

# Create your models here.
class Aircraft(models.Model):
    user_defined_id     =   models.IntegerField()
    passenger_Cap       =   models.IntegerField()

    #calculcated Fields
    fueltank_cap_liters         =      models.FloatField()
    consumpt_per_minute_liters  =    models.FloatField()
    max_minutes =                   models.CharField(max_length=100)

    def __str__(self):
        return str(self.user_defined_id)

    
    @property
    def get_fueltank_cap(self):
        return fuel_cap(self.user_defined_id)
    
    @property
    def get_consumption_per_minute(self): # get consumption per minute via formula module
        return fuel_consumption(self.user_defined_id)
    
    @property
    def get_max_minutes(self): #get max minutes via formula module
        return maximum_minutes(self.user_defined_id, self.fueltank_cap_liters,self.passenger_Cap)
    
    #save calculated fieldsc
    def save(self, *args, **kwargs):
        self.fueltank_cap_liters =self.get_fueltank_cap
        self.max_minutes = self.get_max_minutes
        self.consumpt_per_minute_liters = self.get_consumption_per_minute
        super(Aircraft,self).save(*args, **kwargs)
    