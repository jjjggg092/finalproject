from django.db import models

# Create your models here.
class Balance(models.Model):
    """account"""
    uname = models.CharField(max_length=15)
    money = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.uname} has {self.money}USD to use."

class Spends(models.Model):
    """spends of the user"""
    uname = models.CharField(max_length=15)
    kind = models.CharField(max_length=15)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.uname} wasted {self.quantity} in {self.kind} on {self.date}"

class Ins(models.Model):
    """ins of the user"""
    uname = models.CharField(max_length=15)
    kind = models.CharField(max_length=15)
    save = models.PositiveIntegerField(default=0)
    quantity = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.CharField(max_length=15)
    def __str__(self):
        return f"{self.uname} added {self.quantity} from {self.kind} on {self.date}"

class Sves(models.Model):
    """saves"""
    uname = models.CharField(max_length=15)
    money = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.uname} has {self.money}USD saved."
