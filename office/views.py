from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article
from .forms import ArticleForm


def tape(request):
    articles = Article.objects.all()
    return render(request, 'tape.html', context={'articles': articles})


def view_article(request, pk):
    article = Article.objects.filter(id=pk)
    return render(request, 'view_article.html', context={'article': article})


@login_required
def write_article(request):
    form = ArticleForm
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title')
        article.prev = request.POST.get('prev')
        article.text = request.POST.get('text')
        article.create_preview()
        article.publish()
        return HttpResponseRedirect('/')
    return render(request, 'add_article.html', context={'form': form})


@login_required
def del_article(request, pk):
    article = Article.objects.filter(id=pk)
    article.delete()
    return HttpResponseRedirect('/')


@login_required
def edit_article(request, pk):
    pass
