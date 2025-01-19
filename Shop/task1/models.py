from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(decimal_places=2, max_digits=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    size = models.DecimalField(decimal_places=0, max_digits=8)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='Buyers')
    DecimalField = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    BooleanField = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default='')
    date = models.DateField(auto_now_add=True)
