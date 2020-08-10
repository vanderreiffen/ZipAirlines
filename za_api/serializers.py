from rest_framework import serializers
from .models import Airplane

class AirplaneSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     many = kwargs.pop('many', True)
    #     super(AirplaneSerializer, self).__init__(many=many, *args, **kwargs)

    class Meta:
        model = Airplane
        # fields = ['id','uid','passenger_capacity']
        fields = '__all__'
        read_only_fields = ['model_name','fueltank_cap', 'consumption_per_minute','max_minutes'] 
