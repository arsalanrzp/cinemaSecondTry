import pkgutil
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import ShowTimeSearchForms

# Create your views here.
from ticketing.models import Movie, Cinema, Ticket, ShowTime
from accounts.models import Profile
from django.urls import reverse

def movie_list(request):
    movies = Movie.objects.all()
    count = len(movies)
    context = {
        'movies': movies,
        'count': count
    }
    return render(request, 'ticketing/movie_list.html', context)


def cinema_list(request):
    cinema = Cinema.objects.all()
    count = len(cinema)
    context = {
        'cinemas': cinema,
        'count': count
    }
    return render(request, 'ticketing/cinema_list.html', context)


def movie_details(request, movie_id):

    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie
    }
    return render(request, 'ticketing/movie_details.html', context)


def cinema_details(request, cinema_id):

    cinema = get_object_or_404(Cinema, pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request, 'ticketing/cinema_details.html', context)


@login_required
def ticket_details(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    context = {
        'ticket' : ticket
        }
    return render(request, 'ticketing/ticket_details.html', context)


@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(costumer=request.user.profile).order_by('-order_time')
    context = { 'tickets' : tickets }
    return render(request, 'ticketing/ticket_list.html', context)


@login_required
def showtime_details(request, showtime_id):
    if request.method == 'POST':
        showtime = get_object_or_404(ShowTime, pk=showtime_id)
        user = request.user
        seat_count = int(request.POST['seat_count'])
        try:
            showtime.reserve_seats(seat_count, request.user)
        except Exception as e:
            context = {'error' : e}
            return render(request, 'ticketing/error_for_reserve.html', context)
        else:
            ticket = Ticket.objects.create(sans=showtime, costumer=user.profile, seat_count=seat_count)
            return HttpResponseRedirect(reverse('ticketing:ticket_details', kwargs={'ticket_id':ticket.id}))
    else:
        showtime = get_object_or_404(ShowTime, pk=showtime_id)
        context = {'showtime' : showtime}
        return render(request, 'ticketing/showtime_details.html', context)


@login_required
def showtime_list(request):
    search_form = ShowTimeSearchForms(request.GET)
    showtimes = ShowTime.objects.all()
    if search_form.is_valid() :
        showtimes = showtimes.filter(movie__name__contains=search_form.cleaned_data['movie_name'])
        if search_form.cleaned_data['available_sales']:
            showtimes = showtimes.filter(status=2)
        if search_form.cleaned_data['cinema'] is not None:
            showtimes = showtimes.filter(cinema=search_form.cleaned_data['cinema'])
        minprice, maxprice = search_form.get_price_boundries()
        if minprice is not None:
            showtimes = showtimes.filter(price__gte=minprice)
        if maxprice is not None:
            showtimes = showtimes.filter(price__lte=maxprice)
    context = {
    'showtimes': showtimes,
    'search_form': search_form
    }
    return render(request, 'ticketing/showtime_list.html', context)













#
# def mytime(request):
#     if request.user.is_authenticated and request.user.is_active:
#         now = datetime.now()
#         html = "<html><body>It is now %s.</body></html>" % now
#         return HttpResponse(html)
#     else:
#         return HttpResponse("ure not logged in")
#     # response = HttpResponse()
#     # response.write("<p>Here's the text of the Web page.</p>")
#     # response.write("<p>Here's another paragraph.</p>")
#     # return HttpResponse(response)
