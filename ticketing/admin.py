from django.contrib import admin

# Register your models here.

from ticketing.models import Cinema, Movie, ShowTime, Ticket
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(ShowTime)
admin.site.register(Ticket)
