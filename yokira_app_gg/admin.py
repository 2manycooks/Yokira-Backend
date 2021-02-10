from django.contrib import admin
from .models import Test, ItemType, EnemyType, EnemyImage, Equipment, Backpack, Player, Enemy

# Register your models here.

admin.site.register(Test)
admin.site.register(ItemType)
admin.site.register(EnemyType)
admin.site.register(EnemyImage)
admin.site.register(Equipment)
admin.site.register(Backpack)
admin.site.register(Player)
admin.site.register(Enemy)