"""
TODO module docstring
"""
from django.db import models


# Create your models here.

class Club(models.Model):
    club_name = models.CharField(max_length=45)
    club_ceo = models.CharField(max_length=45)


class VerificationCode(models.Model):
    code = models.TextField()
    participants_limit = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)


class Participant(models.Model):
    class Gender(models.TextChoices):
        NONE = 'N', 'None'
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=1,
        choices=Gender.choices,
        default=Gender.NONE
    )
    date_of_birth = models.DateField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    verification_code = models.ForeignKey(
        VerificationCode, on_delete=models.CASCADE)


class Duel(models.Model):
    participant_one = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="participant_one")
    participant_two = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="participant_two")
    parent_duel = models.ForeignKey('self', on_delete=models.DO_NOTHING)
    winner = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="weiner")
    score_description = models.TextField()


class User(models.Model):
    class UserType(models.TextChoices):
        ADMINISTRATOR = 'A', 'Administrator'
        MODERATOR = 'M', 'Moderator'

    username = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    hashed_password = models.CharField(max_length=45)
    user_type = models.CharField(
        max_length=1,
        choices=UserType.choices,
        default=UserType.MODERATOR
    )


class Tournament(models.Model):
    time = models.TimeField()
    date = models.DateField()
    location = models.CharField(max_length=120)


class Category(models.Model):
    category_name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)


class Tree(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    root_duel = models.ForeignKey(Duel, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
