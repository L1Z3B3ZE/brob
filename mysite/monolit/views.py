from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView
from .forms import *
from .models import *

class IndexView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.order_by('-date_create', '-time_create')[:5]

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

class LoginView(LoginView):
    template_name = 'user/login.html'
    success_url = reverse_lazy('index')
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'user/logout.html'
class ProfileBasket(LoginRequiredMixin, ListView):
    model = Basket
    context_object_name = 'baskets'
    template_name = 'user/profile.html'

def basket_add(request, product_id):
    product = Product.objects.get(id = product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, count=1)
        return redirect('profile')
    else:
        basket = baskets.first()
        basket.count += 1
        basket.save()
        return redirect('profile')

class ProductsAllView(ListView):
    model = Product
    template_name = 'all_products.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.order_by('-date_create', '-time_create')

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
