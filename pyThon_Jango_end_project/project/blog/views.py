from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import ArticleForm, loginForm, RegistrationForm
from django.contrib.auth import login, logout


# Create your views here.


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    sort_field = request.GET.get('sort')

    if sort_field:
        articles = articles.order_by(sort_field)

    context = {
        'title': 'Blog Page',
        'categories': categories,
        'articles': articles

    }

    return render(request, 'blog/index.html', context)


def category_page(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    sort_field = request.GET.get('sort')

    if sort_field:
        articles = articles.order_by(sort_field)

    context = {
        'title': f"Category: {category.title}",
        'articles': articles

    }

    return render(request, 'blog/index.html', context)


def article_detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.views += 1
    article.save()
    articles: objects = Article.objects.all()
    articles = articles.order_by('-views')

    context = {
        'article': article,
        'articles': articles[:4]
    }

    return render(request, 'blog/article_detail.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = Article.objects.create(**form.cleaned_data)
            article.save()
            return redirect('article', article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
        'title': 'Add Movie'
    }

    return render(request, 'blog/article_form.html', context)


def user_login(request):
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = loginForm()

    context = {
        'form': form,
        'title': 'Authentication'
    }

    return render(request, 'blog/user_login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return redirect('register')
    else:
        form = RegistrationForm()

    context = {
        'form': form,
        'title': 'Registration'
    }

    return render(request, 'blog/register.html', context)


def delete_article(request, id):
    article = Article.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('index')

    context = {
        'article': article
    }

    return render(request, 'blog/confirm_delete.html', context)


def update_article(request, id):
    instance = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('article', id)
        else:
            return render('update', id)
    else:
        form = ArticleForm(instance=instance)

    context = {
        'title': 'Update Movie',
        'form': form
    }

    return render(request, 'blog/article_form.html', context)


# def go_back_article(request, id):
#     context = {
#         'id': id
#     }
#
#     return render(request, 'blog/article_detail.html', context)

def about_dev(request):
    return render(request, 'blog/about_dev.html')
