from django.shortcuts import render , get_object_or_404
from .models import Business, ClientService
from core.models import Category
def infos(request):
    business = Business.objects.all().last()
    random_cat = Category.objects.all().order_by('?')[:5]
    sav = ClientService.objects.all()[:4]
    context = {
            'business' : business,
            'sav' : sav,
            'random_cat' : random_cat
        }
    return context
    

