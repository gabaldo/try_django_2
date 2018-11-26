from .models import Article
from .forms import ArticleModelForm
from django.shortcuts import get_object_or_404
from django.urls import reverse

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)

# Create your views here.

class ArticleListView(ListView):
	template_name = 'articles/article_list.html' # <blog>/<model_name>_list.html
	queryset = Article.objects.all()


class ArticleDetailView(DetailView):
	template_name = 'articles/article_detail.html' # <blog>/<model_name>_list.html
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
	form_class = ArticleModelForm
	template_name = 'articles/article_create.html' # <blog>/<model_name>_list.html
	queryset = Article.objects.all()
	# success_url = '/'

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

	# ou
	# def get_success_url(self):
	# 	return '/'
	# mas o padrao adicionado no model é melhor

class ArticleUpdateView(UpdateView):
	form_class = ArticleModelForm
	template_name = 'articles/article_update.html' # <blog>/<model_name>_list.html
	queryset = Article.objects.all()

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)


class ArticleDeleteView(DeleteView):
	template_name = 'articles/article_delete.html' # <blog>/<model_name>_list.html
	# queryset = Article.objects.all()
	# success_url = '/blog'

	def get_object(self):
		id_ = self.kwargs.get('id')
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('articles:article-list')