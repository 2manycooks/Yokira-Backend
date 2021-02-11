from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from yokira_app_gg.models import Test, Equipment, Backpack, Player, Enemy


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username',]

class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('id',
                  'title',
                  'description',
                  'published')

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