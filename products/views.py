from django.http import Http404 #uma outra maneira de apresentar o nao existe
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product

from .forms import ProductForm, RawProductForm


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
    	form.save()
    	form = ProductForm()

    context = {
    	'form': form,
    }

    return render(request, 'products/product_create.html', context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)

#     context = {
#     	'objects': obj,
#     }

#     return render(request, 'products/product_detail.html', context)


def product_detail_view(request, id):
	#obj = Product.objects.get(id=my_id)
	
	# melhor maneira de apresentar o não existe
	obj = get_object_or_404(Product, id=id)
	
	# Outra maneira de apresentar o nao existe
	# try:
	# 	obj = Product.objects.get(id=my_id)
	# except Product.DoesNotExist:
	# 	raise Http404
	context = {
		'object': obj,
	}
	return render(request, "products/product_detail.html", context)

def product_update_view(request, id):
	obj = get_object_or_404(Product, id=id)
	# POST request
	if request.method == 'POST':
		# confirming delete
		obj.delete()
		return redirect('../../../')

	context = {
		'object': obj,
	}
	return render(request, "products/product_delete.html", context)


def product_delete_view(request, id):
	obj = get_object_or_404(Product, id=id)
	# POST request
	if request.method == 'POST':
		# confirming delete
		obj.delete()
		return redirect('../../../')

	context = {
		'object': obj,
	}
	return render(request, "products/product_delete.html", context)


def product_list_view(request):
	queryset = Product.objects.all() # list of objects
	context = {
		'object_list': queryset,
	}
	return render(request, "products/product_list.html", context)