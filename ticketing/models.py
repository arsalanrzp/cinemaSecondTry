from django.db import models

# Create your models here.
from accounts.models import Profile
# from django.contrib.auth import User

class Movie(models.Model):
    """
    Represent a movie
    """
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    length = models.IntegerField()
    year = models.IntegerField()
    description = models.TextField()
    poster = models.ImageField(upload_to='movie_posters/')

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represent a cinema
    """
    name = models.CharField(max_length=20)
    address = models.TextField()
    capacity = models.IntegerField()
    phoneNumber = models.IntegerField()

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    """
    represent a movie in a specified place and specified Time
    """
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    startTime = models.TimeField()
    startDate = models.DateField()
    price = models.IntegerField()
    saleableSeats = models.IntegerField()
    freeSeats = models.IntegerField()
    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    statusChoices = (
        (1, "SALE_NOT_STARTED_YET"),
        (2, "SALE_OPEN"),
        (3, "TICKETS_SOLD"),
        (4, "SALE_CLOSED"),
        (5, "MOVIE_PLAYED"),
        (6, "SHOW_CANCELED")
    )
    status = models.IntegerField(choices=statusChoices)

    def __str__(self):
        return "{}-{}-{}".format(self.movie, self.cinema, self.startTime)

    def reserve_seats(self, seat_count, person):
        assert self.status == 2,'showtime is not available now!'
        assert self.freeSeats >= seat_count, 'there is not enough seats'
        assert self.saleableSeats >= seat_count, 'there is not enough seats'
        assert person.profile.spend(seat_count * self.price), 'you have not enough credit'
        self.freeSeats -= seat_count
        self.saleableSeats -= seat_count
        self.save()
        if self.saleableSeats == 0:
            self.status = 4
        elif self.freeSeats == 0:
            self.status = 3
        return



class Ticket(models.Model):

	"""docstring for Ticket"""

	sans = models.ForeignKey('ShowTime', on_delete=models.CASCADE)
	costumer = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
	seat_count = models.IntegerField(max_length=10)
	order_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} seats for {} reserved by {}".format(self.seat_count, self.sans, self.costumer)
