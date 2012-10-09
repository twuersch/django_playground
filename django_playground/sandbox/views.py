# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Thing
from django.contrib.auth.models import User

def iterate_many_to_many(request):
    owners_as_string = ""
    everyones_thing = Thing.objects.get(name = "Everyone's Thing")
    for owner in everyones_thing.owners.all():
        owners_as_string = owners_as_string + " " + unicode(owner)
    return render(request, "iterate_many_to_many.html", {"owners_as_string": owners_as_string})

def is_many_to_many_save_required(request):
    # check whether a save() is required after an add(). It doesn't seem to be.
    alices_thing = Thing.objects.get(name = "Alice's Thing")
    bob = User.objects.get(username = "bob")
    alices_thing.owners.add(bob)
    alices_thing = Thing.objects.get(name = "Alice's Thing")
    return render(request, "is_many_to_many_save_required.html", {"owners": alices_thing.owners.all()})
