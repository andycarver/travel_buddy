from django.shortcuts import render, redirect
from django.contrib import messages
from models import Travel, User

# Create your views here.
def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    if session_check(request):
        context = {
            'user_travels': Travel.objects.filter(solo_trip__id=request.session['user']['user_id']),
            'joined_travels': Travel.objects.filter(users__id=request.session['user']['user_id']),
            'all_travels': Travel.objects.all()
        }
        return render(request, 'travel/index.html', context)

    return redirect('login:index')

def add_travel(request):
    if session_check(request):
        return render(request, 'travel/add_travel.html')

    return redirect('login:index')

def add_trip(request):
    if session_check(request):
        
        result = Travel.objects.add_trip(request)

        if result[0] == False:
            print_errors(request, result[1])
            return redirect('travel:add_travel')
        
        return redirect('travel:index')

    return redirect('login:index')

def show(request, id):
    if session_check(request):
        context = {
            'travel': Travel.objects.get(id=id),
            'joining': User.objects.filter(travels__id=id)
        }
        return render(request, 'travel/show.html', context)

    return redirect('login:index')

def join_trip(request, id):
    if session_check(request):
        Travel.objects.join_trip(request, id)
        return redirect('travel:show', id)

    return redirect('login:index')

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def logout(request):
    request.session.clear()

    return redirect('login:index')