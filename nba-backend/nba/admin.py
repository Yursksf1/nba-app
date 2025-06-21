from django.contrib import admin
from .models import Team, Player, Game, PlayerStat


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team', 'birth_date', 'height')
    list_filter = ('team',)
    search_fields = ('name', 'team__name')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'team')
        }),
        ('Información personal', {
            'fields': ('birth_date', 'height')
        }),
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'home_team', 'away_team', 'home_score', 'away_score')
    list_filter = ('date', 'home_team', 'away_team')
    search_fields = ('home_team__name', 'away_team__name')
    ordering = ('-date',)


@admin.register(PlayerStat)
class PlayerStatAdmin(admin.ModelAdmin):
    list_display = ('id', 'player', 'game', 'points')
    list_filter = ('game__date', 'player__team')
    search_fields = ('player__name', 'game__home_team__name', 'game__away_team__name')
    raw_id_fields = ('player', 'game')
