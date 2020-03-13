from rest_framework import serializers
from .models import *


class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ['code', 'requirement', 'client', 'number', 'status', 'time', 'id']
