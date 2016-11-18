from django.shortcuts import render, redirect
from models import Travel, User

# Create your views here.
def index(request):
    if session_check(request):
        context = {
            'travel': Travel.objects.all()
        }
        return render(request, "travel/index.html", context)

    return redirect('login:index')


def add_trip(request):
    return render(request, 'travel/add_trip.html')

def create(request):
    Travel.objects.create(destination=request.POST['destination'], description=request.POST['description'], travel_date_from=request.POST['travel_date_from'], travel_date_to=request.POST['travel_date_to']  )
    return redirect('travel:index')


def join(request):
    user = User.objects.get(id=request.POST['user_id'])
    travel = Travel.objects.get(id=request.POST['travel_id'])
    travel.users.add(user)
    return redirect('travel:index')

def show(request, id):
    if session_check(request):
        context = {
            'travel': Travel.objects.get(id=id),
            'user': User.objects.get(id=id),
        }

        return render(request, 'travel/show.html', context)

    return redirect('login:index')

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False