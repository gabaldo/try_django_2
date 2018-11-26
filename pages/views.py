from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	print(request)
	""" return HttpResponse("<h1>Hello World</h1>") """
	return render(request, 'home.html', {})


def about_view(request, *args, **kwargs):

	my_context = {
		'my_text': 'This is about me.',
		'my_number': 4191919191,
		'my_list': [1, 12, 123, 1234, 'Abc']
	}

	return render(request, 'about.html', my_context)


def contact_view(request, *args, **kwargs):
	return render(request, 'contact.html', {})
