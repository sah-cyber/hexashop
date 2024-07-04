from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,FormView
from about.models import About
from categoriya.models import Category
from homeshop.models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from form.models import Contact,ContactForm
from sosialmedia.models import SosialMedia
from django.contrib.messages.views import SuccessMessageMixin




def index(request):
    category_men = Product.published.all().filter(category__name='Kiwi')
    category_women=Product.published.all().filter(category__name='Qadin')
    category_child=Product.published.all().filter(category__name='Usaq')
    #sosial_med = SosialMedia.objects.all()

    context = {'title': 'Ana Sehife',
               'category_men':category_men,
               'category_women':category_women,
               'category_child':category_child,
               #'sosial_med':sosial_med,
                }
    return render(request, 'index.html', context)


# def products(request):
#     products = Product.published.all()
#     paginator = Paginator(products, 2)
#     page = request.GET.get('page')
#     try:
#         page_obj = paginator.get_page(page)
#
#     except PageNotAnInteger:
#         page_obj=paginator.page(1)
#     except EmptyPage:
#         page_obj=paginator.page(paginator.num_pages)
#     context = {
#         'products': page_obj,
#         'title': 'Mehsullarimiz',
#        }
#     return render(request, 'products.html', context)

def about(request):
    about = About.objects.all()
    context = \
        {'title': 'About',
         'about': about
        }
    return render(request, 'about.html', context)


class ProductView(ListView):
    queryset = Product.published.all()
    context_object_name = 'products'
    paginate_by = 4
    template_name = 'products.html'



def product_detail(request, year, month, day, slug, id):
    product = get_object_or_404(Product, status=Product.Status.PUBLISHED, slug=slug, publish__year=year,
                                publish__month=month, publish__day=day, pk=id)
    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)




class ContactForm(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('homeshop:contact')
    success_message = "Sizin Mektub Gonderildi"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        #context['sosial_med']=SosialMedia.objects.all()
        return context

