from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Card, Deck, Player

class PlayerInline(admin.StackedInline):
    model = Player
    can_delete = False
    verbose_name_plural = 'players'

class UserAdmin(BaseUserAdmin):
    inlines = (PlayerInline,)

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Card)
admin.site.register(Deck)
admin.site.register(Player)

