from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Partner,  Faq

class PartnerListView(ListView):
    context_object_name = 'partners'

    model = Partner
    template_name = "partner.html"


# class RealisationListView(ListView):
#     context_object_name = 'realisations'

#     model = Realisation
#     template_name = "realisation.html"


# class RealisationDetailView(DetailView):
#     model = Realisation
#     template_name = "realisation-detail.html"

class FAQListView(ListView):
    model = Faq
    template_name = "faq.html"

    def get_queryset(self):
        faq = Faq.objects.filter(actif=True)
        return faq
    