from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Article, TimePeriod
from .forms import ArticleForm, TimePeriodForm


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
        if request.FILES.get('photo') is not None:
            article.photo = request.FILES.get('photo')
        article.create_preview()
        article.save()
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


@login_required
def view_periods(request):
    form = TimePeriodForm
    if request.method == 'POST':
        form = TimePeriodForm(request.POST)
        if form.is_valid():
            period = form.save(commit=False)
            period.save()
            return HttpResponseRedirect('/')
    periods = TimePeriod.objects.all()
    return render(request, 'date_manager.html', context={'periods': periods, 'form': form})


@login_required
def del_period(request, pk):
    period = TimePeriod.objects.filter(id=pk)
    period.delete()
    return HttpResponseRedirect('/')
