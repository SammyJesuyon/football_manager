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
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    
    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)
    
    @classmethod
    def create(cls, first_name, last_name, age, country, team, position):
        player = cls(first_name=first_name, last_name=last_name, age=age, country=country, team=team, position=position)
        return player
        
gk1 = Player.create('GK1' 'GK', 18, 'USA', 'team1', 'goal_keeper', 1000000)
gk2 = Player.create('GK2' 'GK', 18, 'USA', 'team1', 'goal_keeper', 10000000)
gk3 = Player.create('GK3' 'GK', 18, 'USA', 'team1', 'goal_keeper', 10000000)
def1 = Player.create('DEF1' 'DEF', 18, 'USA', 'team1', 'defender', 10000000)
def2 = Player.create('DEF2' 'DEF', 18, 'USA', 'team1', 'defender', 10000000)
def3 = Player.create('DEF3' 'DEF', 18, 'USA', 'team1', 'defender', 10000000)
def4 = Player.create('DEF4' 'DEF', 18, 'USA', 'team1', 'defender', 10000000)
def5 = Player.create('DEF5' 'DEF', 18, 'USA', 'team1', 'defender', 10000000)
def6 = Player.create('DEF6' 'DEF', 18, 'USA', 'team1', 'defender', 10000000)
mid1 = Player.create('MID1' 'MID', 18, 'USA', 'team1', 'midfielder', 10000000)
mid2 = Player.create('MID2' 'MID', 18, 'USA', 'team1', 'midfielder', 10000000)
mid3 = Player.create('MID3' 'MID', 18, 'USA', 'team1', 'midfielder', 10000000)
mid4 = Player.create('MID4' 'MID', 18, 'USA', 'team1', 'midfielder', 10000000)
mid5 = Player.create('MID5' 'MID', 18, 'USA', 'team1', 'midfielder', 10000000)
mid6 = Player.create('MID6' 'MID', 18, 'USA', 'team1', 'midfielder', 10000000)
att1 = Player.create('ATT1' 'ATT', 18, 'USA', 'team1', 'attacker', 10000000)
att2 = Player.create('ATT2' 'ATT', 18, 'USA', 'team1', 'attacker', 10000000)
att3 = Player.create('ATT3' 'ATT', 18, 'USA', 'team1', 'attacker', 10000000)
att4 = Player.create('ATT4' 'ATT', 18, 'USA', 'team1', 'attacker', 10000000)
att5 = Player.create('ATT5' 'ATT', 18, 'USA', 'team1', 'attacker', 10000000)