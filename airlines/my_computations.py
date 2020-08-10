import math
import random
import uuid
import datetime

def generate_model_number():
    #returns random sequence of strings for the model number
    return uuid.uuid4().hex[:6].upper()


def fuel_cap(uid : int)-> int:
    return uid * 200 #user defined id multiplied by 200 

def fuel_consumption(uid : int) -> float:
    consumpt_per_min =round( math.log(uid) * .80, 4)
    return  consumpt_per_min#logarithm of the user_defined_id multiplied by .80

def maximum_minutes(uid: int, fuel_tank_cap : int, passenger_count : int) -> float:
    init_duration = fuel_tank_cap / fuel_consumption(uid)
    addon_duration = passenger_count * 0.002
    time = str(datetime.timedelta(minutes= init_duration + addon_duration)) #convert float to time format
    return time