from django.urls import path


from .views import (
    #blog_list_view,
    #blog_detail_view,
    ArticleCreateView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    )

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
]