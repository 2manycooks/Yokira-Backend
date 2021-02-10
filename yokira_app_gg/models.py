from django.db import models
from django.contrib.auth.models import User, Group

""" === Join Tables/FK's === """

# Is an FK inside Equipment. Stores item type (Potion, Sword, Helm, etc).
class ItemType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

# Is an FK inside Enemy. Defines enemy type (for purpose of special abilities, image, etc)
class EnemyType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

# Is an FK inside Enemy. Stores location of img source.
class EnemyImage(models.Model):
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

"""  === Base Models  === """

class Test(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)

class Equipment(models.Model):
    item_type = models.OneToOneField(ItemType, on_delete=models.RESTRICT)
    is_equipped = models.BooleanField(default=False)
    min_atk = models.IntegerField()
    max_atk = models.IntegerField()
    min_def = models.IntegerField()
    max_def = models.IntegerField()

    def __str__(self):
        return self.item_type.name
    

# Player model has One-To-One relation with Backpack, with inidividual instances of the equipment model.
class Backpack(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    slot_1 = models.ForeignKey(Equipment, related_name="bp_slot_1", on_delete=models.CASCADE, default= None, blank=True, null= True)
    slot_2 = models.ForeignKey(Equipment, related_name="bp_slot_2", on_delete=models.CASCADE, default= None, blank=True, null= True)
    slot_3 = models.ForeignKey(Equipment, related_name="bp_slot_3", on_delete=models.CASCADE, default= None, blank=True, null= True)
    slot_4 = models.ForeignKey(Equipment, related_name="bp_slot_4", on_delete=models.CASCADE, default= None, blank=True, null= True)
    slot_5 = models.ForeignKey(Equipment, related_name="bp_slot_5", on_delete=models.CASCADE, default= None, blank=True, null= True)
    slot_6 = models.ForeignKey(Equipment, related_name="bp_slot_6", on_delete=models.CASCADE, default= None, blank=True, null= True)

    def __str__(self):
        return self.owner.player_name
    



class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    hp = models.IntegerField()
    mp = models.IntegerField()
    samurai = 'SM'
    shinobi = 'SH'
    monk = 'MK'
    player_class_choices = [
        (samurai, 'Samurai'),
        (shinobi, 'Shinobi'),
        (monk, 'Monk')
    ]
    player_class = models.CharField(max_length=2, choices=player_class_choices)
    backpack_contents = models.OneToOneField(Backpack, on_delete=models.CASCADE, default=Backpack)


class Enemy(models.Model):
    enemy_name = models.CharField(max_length=20)
    enemy_type = models.ForeignKey(EnemyType, on_delete=models.CASCADE, default="")
    enemy_level = models.IntegerField(default=1)
    enemy_image = models.OneToOneField(EnemyImage, on_delete=models.RESTRICT, default="")
    min_atk = models.IntegerField()
    max_atk = models.IntegerField()
    min_def = models.IntegerField()
    max_def = models.IntegerField()
