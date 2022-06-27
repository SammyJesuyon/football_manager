from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField


class Manager(models.Model):
    # avatar = models.ImageField(null=True, blank=True)
    username = models.CharField(max_length=50, unique=True, blank=False, null=False, default='manager')
    first_name = models.CharField(max_length=50, default='name1', null=False, blank=False)
    last_name = models.CharField(max_length=50, default='name2', null=False, blank=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')

    def __str__(self):
        return str(self.email)
    
class Team(models.Model):
    name = models.CharField(max_length=100, default='TeamName', null=False, blank=False)
    country = CountryField()
    cash = models.DecimalField(max_digits=20, default=5000000.00, decimal_places=2, verbose_name='cash in $')
    team_value = models.DecimalField(max_digits=20, default=20000000.00, decimal_places=2, verbose_name='team value in $')
    manager = models.OneToOneField(Manager, on_delete=models.CASCADE, related_name='teams')
    
    def __str__(self):
        return str(self.name)
    
position_choices =(
    ('goal_keeper', 'Goal Keeper'),
    ('defender', 'Defender'),
    ('midfielder', 'Midfielder'),
    ('attacker', 'Attacker'),
)
    
class Player(models.Model):
    
    first_name = models.CharField(max_length=100, default='FirstName', null=False)
    last_name = models.CharField(max_length=100, default='LastName', null=False)
    country = CountryField()
    age = models.IntegerField(validators=[MinValueValidator(18), 
                                          MaxValueValidator(40)], default=18, null=False, blank=False)
    position = models.CharField(max_length=100, default='position', null=False, choices=position_choices)
    value = models.DecimalField(max_digits=100, default=1000000.00, decimal_places=2, verbose_name='value in $')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
    
class Transfer(models.Model):
    asking_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='asking price in $')
    