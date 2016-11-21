from __future__ import unicode_literals
from ..login.models import User
from django.db import models
from datetime import date, datetime
from dateutil.parser import parse as parse_date

class TravelManager(models.Manager):
    def add_trip(self, request):
        errors = self.trip_validations(request)

        if errors:
            return (False, errors)

        user = User.objects.get(id=request.session['user']['user_id'])

        Travel.objects.create(destination=request.POST['destination'], description=request.POST['description'], travel_date_from=request.POST['travel_date_from'], travel_date_to=request.POST['travel_date_to'], solo_trip=user)

        return (True, errors)

    def join_trip(self, request, id):
        user = User.objects.get(id=request.session['user']['user_id'])

        travel = Travel.objects.get(id=id)

        travel.users.add(user)

    def trip_validations(self, request):
        errors = []

        try:
            travel_date_from = parse_date(request.POST['travel_date_from']).date()
            travel_date_to = parse_date(request.POST['travel_date_to']).date()
        except ValueError:
            errors.append('Please add a start and end date.')
            if not request.POST['destination']:
                errors.append('Please add a destination.')
            if not request.POST['description']:
                errors.append('Please add a description.')
            return errors
            
        if travel_date_from < date.today():
            errors.append('Start date can not be before today.')
        if travel_date_from > travel_date_to:
            errors.append('Return date must be after or same as the start date.')
        if not request.POST['destination']:
            errors.append('Please add a destination.')
        if not request.POST['description']:
            errors.append('Please add a description.')

        return errors
# Create your models here.
class Travel(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    travel_date_from = models.DateField()
    travel_date_to = models.DateField()
    solo_trip = models.ForeignKey(User, related_name='trip')
    users = models.ManyToManyField(User, related_name='travels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TravelManager()