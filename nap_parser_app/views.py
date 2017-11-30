from django.shortcuts import render, redirect
from .forms import SimpleForm
from redis.client import Redis
from django.views.generic import ListView
from .models import Product, Price

client = Redis()

def index(request):
    if request.method == "POST":
        form = SimpleForm(request.POST)
        if form.is_valid():
            category = 'https://www.net-a-porter.com/ua/en/d/Shop/' + request.POST['category']
            client.lpush('n_a_p_spider:start_urls', category)
            return redirect('/success')
    else:
        form = SimpleForm()
    return render(request, 'main.html', {'form': form})

# Create your views here.
def success(request):
    return render(request, template_name="success.html")

class ProductsPage(ListView):
    template_name = 'products.html'
    model = Product
    context_object_name = 'products'

class PricesPage(ListView):
    template_name = 'prices.html'
    model = Price
    context_object_name = 'prices'