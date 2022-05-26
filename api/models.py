"""
TODO module docstring
"""
import uuid
from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class Staff(models.Model):
    class UserType(models.TextChoices):
        ADMINISTRATOR = 'A', 'Administrator'
        MODERATOR = 'M', 'Moderator'

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    type = models.CharField(
        max_length=1,
        choices=UserType.choices,
        default=UserType.MODERATOR
    )

class Category(models.Model):
    """
    TODO docstring
    """
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=45)

class Club(models.Model):
    """
    TODO docstring
    """
    name = models.CharField(max_length=45)
    ceo = models.CharField(max_length=45)
    email = models.CharField(max_length=45)

class VerificationCode(models.Model):
    """
    TODO docstring
    """
    def get_random_code(self, length = 6) -> str:
        """
            Generate random code
        """
        return uuid.uuid4().hex.upper()[0:length]

    code = models.TextField(default=get_random_code)
    participants_limit = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class Participant(models.Model):
    """
    TODO docstring
    """
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Duel(models.Model):
    participant_one = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="participant_one", default=None, blank=True, null=True)
    participant_two = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="participant_two", default=None, blank=True, null=True)
    parent_duel = models.ForeignKey('self', on_delete=models.DO_NOTHING, default=None, blank=True, null=True)
    winner = models.ForeignKey(
        Participant, on_delete=models.CASCADE, related_name="weiner", default=None, blank=True, null=True)
    score_description = models.TextField()


""" class User(models.Model):
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
    ) """


class Tournament(models.Model):
    """
    TODO docstring
    ! dajngo DateTime format: YYYY-MM-DD HH:MM
    """
    name = models.CharField(max_length=45)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=45)
    email = models.CharField(max_length=45)


class Tree(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    root_duel = models.ForeignKey(Duel, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
