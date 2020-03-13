from rest_framework import serializers
from index.models import *


class indexSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']