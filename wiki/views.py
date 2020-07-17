from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from wiki.models import Article
from wiki.forms import ArticleForm


class ArticleListView(ListView):
    """ Renders a list of all Articles. """
    model = Article

    def get(self, request):
        """ GET a list of Articles. """
        articles = self.get_queryset().all()
        return render(request, 'list.html', {
          'articles': articles
        })

class ArticleDetailView(DetailView):
    """ Renders a specific article based on it's slug."""
    model = Article

    def get(self, request, slug):
        """ Returns a specific wiki article by slug. """
        article = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'article.html', {
          'article': article
        })

class ArticleCreateView(CreateView):

  def get(self, request, *args, **kwargs):
      context = {'form': ArticleForm()}
      return render(request, 'create.html', context)

  def post(self, request, *args, **kwargs):
    form = ArticleForm(request.POST)
    if form.is_valid():
        page = form.save()
        return HttpResponseRedirect(reverse_lazy('wiki-details-page', args=[page.slug]))
    return render(request, 'create.html', {'form': form})
