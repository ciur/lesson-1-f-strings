from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(
        max_length=100
    )
    last_name = models.CharField(
        max_length=100
    )
    age = models.IntegerField()

    elo_rating = models.IntegerField()
    total_games_count = models.IntegerField()
    complete_games_count = models.IntegerField()
