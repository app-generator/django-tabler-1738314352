# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Club(models.Model):

    #__Club_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    league = models.CharField(max_length=255, null=True, blank=True)

    #__Club_FIELDS__END

    class Meta:
        verbose_name        = _("Club")
        verbose_name_plural = _("Club")


class Player(models.Model):

    #__Player_FIELDS__
    foot_preference = models.CharField(max_length=255, null=True, blank=True)
    birthdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")


class Clubhistory(models.Model):

    #__Clubhistory_FIELDS__
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Clubhistory_FIELDS__END

    class Meta:
        verbose_name        = _("Clubhistory")
        verbose_name_plural = _("Clubhistory")


class Match(models.Model):

    #__Match_FIELDS__
    home_team = models.ForeignKey(Club, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Club, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    video = models.CharField(max_length=255, null=True, blank=True)
    home_score = models.IntegerField(null=True, blank=True)
    away_score = models.IntegerField(null=True, blank=True)

    #__Match_FIELDS__END

    class Meta:
        verbose_name        = _("Match")
        verbose_name_plural = _("Match")


class Performance(models.Model):

    #__Performance_FIELDS__
    non_penalty_goal = models.IntegerField(null=True, blank=True)
    shots_total = models.IntegerField(null=True, blank=True)
    assists = models.IntegerField(null=True, blank=True)
    shots_creating_action = models.IntegerField(null=True, blank=True)
    pass_attempted = models.IntegerField(null=True, blank=True)
    pass_completed = models.IntegerField(null=True, blank=True)
    tackles = models.IntegerField(null=True, blank=True)
    interceptions = models.IntegerField(null=True, blank=True)
    blocks = models.IntegerField(null=True, blank=True)
    clearances = models.IntegerField(null=True, blank=True)
    aerials_won = models.IntegerField(null=True, blank=True)
    player_in_match = models.ForeignKey(Player, on_delete=models.CASCADE)
    match_performed = models.ForeignKey(Match, on_delete=models.CASCADE)
    progressive_pass = models.IntegerField(null=True, blank=True)
    progressive_carries = models.IntegerField(null=True, blank=True)
    successful_take_ons = models.IntegerField(null=True, blank=True)
    touches = models.IntegerField(null=True, blank=True)

    #__Performance_FIELDS__END

    class Meta:
        verbose_name        = _("Performance")
        verbose_name_plural = _("Performance")


class Scout(models.Model):

    #__Scout_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    scout_club = models.ForeignKey(Club, on_delete=models.CASCADE)
    experience = models.IntegerField(null=True, blank=True)

    #__Scout_FIELDS__END

    class Meta:
        verbose_name        = _("Scout")
        verbose_name_plural = _("Scout")


class Playermatchinsight(models.Model):

    #__Playermatchinsight_FIELDS__
    player_assessed = models.ForeignKey(Player, on_delete=models.CASCADE)
    match_assessed = models.ForeignKey(Match, on_delete=models.CASCADE)
    scout_observing = models.ForeignKey(Scout, on_delete=models.CASCADE)
    technical_skill = models.IntegerField(null=True, blank=True)
    game_awareness = models.IntegerField(null=True, blank=True)
    ball_control = models.IntegerField(null=True, blank=True)
    sprinting_speed = models.IntegerField(null=True, blank=True)
    handling_speed = models.IntegerField(null=True, blank=True)
    winning_mindset = models.IntegerField(null=True, blank=True)
    motivation_drive = models.IntegerField(null=True, blank=True)

    #__Playermatchinsight_FIELDS__END

    class Meta:
        verbose_name        = _("Playermatchinsight")
        verbose_name_plural = _("Playermatchinsight")



#__MODELS__END
