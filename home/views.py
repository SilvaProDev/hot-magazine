from django.shortcuts import render
from django.http import HttpResponse
from .models import Produit, Category

# Create your views here.
def index(request):
    produit = Produit.objects.filter().order_by('-id')[:5]
    latest = Produit.objects.filter().order_by('?')[:3]
    categorie = Category.objects.all()
    post = Category.objects.filter(status=False)

    context = {'produit':produit, 'categorie':categorie, 'post':post, 'latest':latest}
    
    return render(request, 'pages/index.html', context)

def single_post(request):
    # produits = Produit.objects.get(pk=id)
    # context = {'produits':produits}
    return render(request, 'pages/single-post.html')

def world(request):
    return render(request, 'pages/news-category4.html')

def travel(request):
    return render(request, 'pages/news-category3.html')

def tech(request):
    return render(request, 'pages/news-category2.html')

def fashion(request):
    return render(request, 'pages/news-category6.html')

def video(request):
    return render(request, 'pages/video.html')

def sport(request):
    return render(request, 'pages/news-category5.html')

def food_healt(request):
    return render(request, 'pages/news-category1.html')

def autor_list(request):
    return render(request, 'pages/autor-list.html')

