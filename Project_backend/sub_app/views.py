from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menuitems (request, dish):
    items = {
        'pasta': 'A plate of pasta',
        'moimoi': 'Some moimoi',
        'garri': 'Some groceries',
    }

    description = items[dish]

    return HttpResponse( f"<h2> {dish} </h2>" + description)


def drinks (request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'refreshment',
    }

    choice_of_drink = drink[drink_name]

    return HttpResponse( f"<h2> {drink_name} </h2>" + choice_of_drink)
