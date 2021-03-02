from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse
import csv

# Create your views here.


def index(request):
    return HttpResponse("<h2>Hello, You are at the product index.</h2>")


# Displaying Product Details
def archive(request):
    res = Product.objects.all()
    return render(request, 'archive.html', {'res': res})


# Displaying details of product based on product id
def detail(request, prod_id):
    product = get_object_or_404(Product, pk=prod_id)
    return render(request, 'detail.html', {'product': product})


# Creating a product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Product Record Added")     # Response to a product is added
        else:
            form = ProductForm(request.POST)
            return render(request, 'addproduct.html', {'form': form})
    else:
        form = ProductForm()
        return render(request, 'addproduct.html', {'form': form})


# Generating a csv file consisting of product details
def generate_csv(request):
    resp = HttpResponse(content_type='text/csv')
    resp['Content-Disposition'] = 'attachment; filename="product.csv"'
    products = Product.objects.all()
    writer = csv.writer(resp, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Product_id', 'Product_name', 'Quantity'])
    for prod in products:
        writer.writerow([prod.product_id, prod.product_name, prod.qty])
    return resp




