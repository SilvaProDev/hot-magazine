from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Produit, Category
from .forms import SignUpForm, SearchForm

# Create your views here.
def index(request):
    produit = Produit.objects.filter().order_by('-id')[:5]
    latest = Produit.objects.filter().order_by('?')[:3]
    categorie = Category.objects.all()
    post = Category.objects.filter(status=False)

    context = {'produit':produit, 'categorie':categorie, 'post':post, 'latest':latest}
    
    return render(request, 'pages/index.html', context)

def contact_us(request):
    
    return render(request, 'pages/contact.html')

def signup(request):
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password = form.cleaned_data('password')
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, 'Votre compte a été creer avec succes')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'erreur de connection')
            return HttpResponseRedirect('/contact_us')
    else:
        form = SignUpForm()
    data = {form:'form'}
    return render(request, 'pages/contact.html', data)

def login_in(request):
    if request.method=='POST':
        
        username = request.POST['username']
        password = request.POSt['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.succes(request, 'Vous etes bien conecté')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Erreur de connection')
            return HttpResponseRedirect('/contact_us')

    return render(request, 'pages/contact.html')

def search(request):
    if request.method=='POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']

            if query:
                produit = Produit.objects.filter(titre__icontains=query)

                if produit:
                    data = {'produit':produit, 'query':query}
                    return render(request, 'pages/search.html', data)
                else:
                    messages.success(request, 'pas de produits correspondant ce nom')
            else:
                return HttpResponseRedirect('/search/')

    return render(request, 'pages/search.html')
           
    


            










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

