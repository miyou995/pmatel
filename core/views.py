from django.db.models import Q 
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, request
from .forms import ContactForm
from delivery.models import Wilaya, Commune
from django.views.generic import TemplateView, DetailView, ListView, CreateView, View
from .models import Brand, Gamme, Product, Category, Solution
from business.models import Business, ThreePhotos, Slide, Counter, LargeBanner,ClientService, Partner
from cart.forms import CartAddProductForm
from business.models import Counter
from .filters import ProductFilter
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from cart.forms import CartAddProductForm
from django.db.models import F

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_products"] = Product.objects.filter(top=True, new=True, actif=True)
        context["top_products"] = Product.objects.filter(top=True, actif=True)
        context["big_slides"]   = Slide.objects.filter(actif=True)
        context["solutions"]   = Solution.objects.all()[:3]
        # context["dual_banners"] = DualBanner.objects.all()[:2]
        context["large_banner"] = LargeBanner.objects.last()
        context["random_cat"]   = Category.objects.all()
        all_cat = Category.objects.all()
        cat_list = []
        for cat in all_cat:
            if cat.products.all().count() > 0:
                cat_list.append(cat)
        context["random_cat"] = cat_list[:3]
        return context


class AboutView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["counters"] = Counter.objects.filter(actif=True)[:4]
        context["processes"] = ClientService.objects.filter(actif=True)[:4]
        context["clients"] = Partner.objects.filter(actif=True)
        return context

class VirementBancaireView(TemplateView):
    template_name = "paiement/virement-bancaire.html"

class CarteBancaireView(TemplateView):
    template_name = "paiement/carte-bancaire.html"

class PaiementView(TemplateView):
    template_name = "paiement/paiement.html"

class PaiementEspecesView(TemplateView):
    template_name = "paiement/paiement-especes.html"



class EchangeView(TemplateView):
    template_name = "livraison/echange.html"

class LivraisonView(TemplateView):
    template_name = "livraison/livraison.html"

class RetourView(TemplateView):
    template_name = "livraison/retours.html"

class SolutionListView(ListView):
    template_name = "solutions.html"
    context_object_name = 'solutions'
    model = Solution

class SolutionDetailView(DetailView):
    template_name = "solution-detail.html"
    model = Solution

def product_detail(request):
    product = Product.objects.get(id=Product.objects.first().id)
    return render(request, 'snipetts/product-modal.html', {'product': product})


# class ProductsView(ListView):
#     context_object_name = 'products'
#     model = Product
#     template_name = "products.html"
#     paginate_by = 24
#     def get_queryset(self):
#         try:
#             param = self.request.GET.get('search')
#             # print('category', param)
#             if param == 'all':
#                 category = Category.objects.filter(actif=True)
#                 products = Product.objects.filter(actif=True)
            
#             elif param is None:
#                 category = Category.objects.filter(actif=True)
#                 products = Product.objects.filter(actif=True)
#             else:
#                 category = Category.objects.get(id = param)
#                 products = Product.objects.filter(category__in=category.get_descendants(include_self=True))
#         except:
#             try:
#                 new = self.request.GET.get('new')
#                 if new == 'new':
#                     products = Product.objects.filter(new=True, actif=True)
#                 elif new == 'promo':
#                     products = Product.objects.filter(old_price=True, actif=True)
#                 else:
#                     pass
#             except:
#                 category = Category.objects.filter(actif=True)
#                 products = Product.objects.filter(actif=True)
#         query = self.request.GET.get('name')
#         if query:
#             # print('query', query)
#             qs = products.search(query=query)
#             # print('les produits ')
#         else:
#             # print('les ELSEEEE ', products)
#             qs = products
#         return qs
#         # except:
#         #     print(' kamel les produits kharjou :) excepty !!!')
#         #     return super().get_queryset() 
        
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         if self.request.GET.get('category'):
#             try:
#                 category = self.request.GET.get('category')
#                 if category == 'all':                
#                     context["category"] = Category.objects.filter(actif=True)
#                 else:                
#                     context["category"] = Category.objects.get(id = category)
#             except:
#                 pass
#         context["brands"] = Brand.objects.filter(actif=True)
#         gammes = Gamme.objects.filter(actif=True).exclude(name=F('brand__name'))
#         context["gammes"] = gammes
#         # context["filters"] = ProductFilter(self.request.GET, queryset= self.get_queryset())
#         # context["products"] = Product.objects.all()
#         return context




def products_view(request):
    context = {}
    context['category_filter'] = True
    context['product_categories'] = Category.objects.filter(actif=True)
    
    category = Category.objects.filter(actif=True)
    products = Product.objects.filter(actif=True)
    category_param = request.GET.get('category')
    brand_param = request.GET.get('brand')
    new_param = request.GET.get('new')
    promo_param = request.GET.get('promo')
    pack_param = request.GET.get('packs')

    if category_param :
        if category_param != 'all':
            context['category_filter'] = False
            category = Category.objects.get(id = category_param)
            products = Product.objects.filter(category__in=category.get_descendants(include_self=True), actif=True)
    if new_param:
        products = Product.objects.filter(new=True, actif=True)
    elif promo_param:
        products = Product.objects.filter(old_price__isnull=False, actif=True)
    elif pack_param:
        products = Product.objects.filter(is_pack=True, actif=True)
    elif brand_param:
        try:
            products = Product.objects.filter(actif=True, brand__id=brand_param)
        except:
            products = Product.objects.filter(actif=True, brand__name__iexact=brand_param)
        context['category_filter'] = False
        # context['product_categories'] = Category.objects.filter(actif=True, products__brand=brand_param)
        print('les produits d la marque ', products)
    else:
        pass
    # print('request', request.GET)
    products_qs = products
    if request.GET.get('query'):
        products = ProductFilter(request.GET, queryset= Product.objects.all())
        products_qs = products.qs
        print('le cash ', request.GET)
    # context['products'] = products.qs[:30]
    context['filter'] = products
    context["category"] = category
    paginator = Paginator(products_qs, 15)
    page = request.GET.get('page')
    print('params => ', request.GET.copy())
    get_copy = request.GET.copy()
    try:
        context['products'] = paginator.page(page)
    except PageNotAnInteger:
        context['products'] = paginator.page(1)
    except EmptyPage:
        context['products'] = paginator.page(paginator.num_pages)
    parameters = get_copy.pop('page', True) and get_copy.urlencode()
    context['parameters'] = parameters
    print('la cateogrie', category)

    if request.htmx:
        return render(request, 'snippets/htmx-products.html', context)
    return render(request, 'products.html', context)

def filtred_htmx_products(request):
    context = {}
    print('request', request.GET)
    products = ProductFilter(request.GET, queryset= Product.objects.all())
    context['products'] = products.qs
    print('context[products]', context['products'])
    # return render(request, 'snippets/htmx_products.html', context)
    return render(request, 'snippets/htmx_products.html', context)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = "product-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        random_related = Product.objects.filter(actif=True).order_by('?')[:4] 
        context["wilayas"] = Wilaya.objects.filter(active=True).order_by('name') 
        prod = self.get_object()
        print('le produit', prod)
        category = prod.category
        print('la categorir', category)
        products =  Product.objects.filter(category=category, actif=True)

        same_category_products = products.exclude(id=prod.id).order_by('?')[:8]
        print('related products]', products)
        if same_category_products :
            context["related_products"] = same_category_products
        else:
            context["related_products"] = random_related
        print('context[products]', context["related_products"])

        context["related_products_count"] = products.count() - 1
        context['form'] = CartAddProductForm()
        # context['atributes'] = prod.product_type.atributes.all()
        return context

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
  
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        message = 'Une erreur est survenue, veuillez réessayer.'
        success = False
        try:
            #save the form   
            if form.is_valid():
                form.save()
                #messages.success(request, 'Votre message a bien été envoyé')
                message = 'Votre message a bien été envoyé!'
                success = True
                print(success)
                return render(request, 'other/contact.html', {'message': message, 'success': success})
            else:
                print(success)
                message = 'Une erreur est survenue, veuillez réessayer.'
                return render(request, 'contact.html', {'message': message, 'failure': True})
        except:
            return render(request, 'contact.html', {'message': message, 'failure': True})
        return render(request, 'contact.html', {'message': message, 'failure': True})




# def set_if_not_none(mapping, key, value):
#     if value is not None:
#         mapping[key] = value

