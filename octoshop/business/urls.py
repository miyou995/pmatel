from django.urls import path
from .views import PartnerListView,  FAQListView

app_name = 'business'

urlpatterns = [
   path('partenaires', PartnerListView.as_view(), name='partner'),
   # path('projets', RealisationListView.as_view(), name='realisation'),
   path('faq', FAQListView.as_view(), name='faq'),
   # path('checkout', CheckoutView.as_view(), name='CheckoutView'),
]

