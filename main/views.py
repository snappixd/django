from django.shortcuts import render
from .models import Product

def index(request):
	products = Product.objects.all()
	return render(request, "index.html", {'title': 'Главная', 'products': products})

def about_product(request, slug):
	product_title = Product.objects.get(slug=slug).title
	product_description = Product.objects.get(slug=slug).description
	product_material = Product.objects.get(slug=slug).material
	product_length = Product.objects.get(slug=slug).length
	product_slug = Product.objects.get(slug=slug).slug
	product_img = Product.objects.get(slug=slug).img
	product_price = Product.objects.get(slug=slug).price
	context = {
		'product_title': product_title,
		'product_description': product_description,
		'product_material': product_material,
		'product_length': product_length,
		'product_slug': product_slug,
		'product_img': product_img,
		'product_price': product_price,
	}


	return render(request, "about_product.html", context)


