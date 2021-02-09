from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    hp = models.IntegerField()
    mp = models.IntegerField()
    player_class = models.CharField(max_length=20)
    backpack_contents = models.OneToOneField(Backpack)

class Equipment(models.Model):
    item_type = models.OneToOneField(ItemType)
    is_equipped = models.BooleanField(default=False)
    min_atk = models.IntegerField()
    max_atk = models.IntegerField()
    min_def = models.IntegerField()
    max_def = models.IntegerField()

class Enemy(models.Model):
    enemy_name = models.CharField(max_length=20)
    enemy_type = models.CharField(max_length=20)
    enemy_level = models.IntegerField(default=1)
    min_atk = models.IntegerField()
    max_atk = models.IntegerField()
    min_def = models.IntegerField()
    max_def = models.IntegerField()

class Backpack(models.Model):
    backpack_slot_1 = models.OneToOneField(Equipment, on_delete=SET_NULL, null=True)
    backpack_slot_2 = models.OneToOneField(Equipment, on_delete=SET_NULL, null=True)
    backpack_slot_3 = models.OneToOneField(Equipment, on_delete=SET_NULL, null=True)
    backpack_slot_4 = models.OneToOneField(Equipment, on_delete=SET_NULL, null=True)
    backpack_slot_5 = models.OneToOneField(Equipment, on_delete=SET_NULL, null=True)
    backpack_slot_6 = models.OneToOneField(Equipment, on_delete=SET_NULL, null=True)
