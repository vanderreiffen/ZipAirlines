from rest_framework import serializers
from airlines.models import Aircraft

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = '__all__'
        read_only_fields = [
            'fueltank_cap_liters',
            'consumpt_per_minute_liters',
            'max_minutes']
        
        
