
from rest_framework import serializers
from yokira_app_gg.models import Test, Equipment, Backpack, Player, Enemy


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'
        

class BackpackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backpack
        """ fields = '__all__' """
        exclude = ['id']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        """ field = '__all__' """
        exclude = ['id']
class EnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enemy
        """ field = '__all__' """
        exclude = ['id']