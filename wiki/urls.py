from django.urls import path
from wiki.views import ArticleListView, ArticleDetailView, ArticleCreateView


urlpatterns = [
    path('', ArticleListView.as_view(), name='wiki-list-page'),
    path('w/<str:slug>/', ArticleDetailView.as_view(), name='wiki-details-page'),
    path('create/', ArticleCreateView.as_view(), name='create'),
]
