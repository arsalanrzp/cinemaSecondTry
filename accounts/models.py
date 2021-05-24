from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=11)
    male = 1
    female = 2
    Gender_choices = ((1, 'male'), (2, 'female'))
    gender = models.IntegerField(choices=Gender_choices, null=True, blank=True)
    address = models.TextField()
    balance = models.IntegerField()

    def __str__(self):
        return self.user.get_full_name()

    def increase_credit(self, amount):
        self.balance += amount
        self.save()

    def spend(self, amount):
        if self.balance < amount:
            return False
        else:
            self.balance -= amount
            self.save()
            return True

    def supply(self):
        return self.balance
