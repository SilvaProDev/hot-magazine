from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
from django.conf import settings

from .models import Produit, Category, UserProfile, ContactMessage
from .forms import SignupForm, SearchForm, ContactForm

# Create your views here.
def index(request):
    produit = Produit.objects.filter().order_by('-id')[:5]
    latest = Produit.objects.filter().order_by('?')[:3]
    categorie = Category.objects.all()
    post = Category.objects.filter(status=False)

    context = {'produit':produit, 'categorie':categorie, 'post':post, 'latest':latest}
    
    return render(request, 'pages/index.html', context)

@csrf_exempt
def contact_us(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.save()

            subject="Test de mail"
            from_email= settings.EMAIL_HOST_USER
            to_email= [data.email]
            message_body="""Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio. Quisque volutpat mattis eros. Nullam malesuada erat 
            ut turpis. Suspendisse urna nibh, viverra non, semper suscipit, posuere a, pede. Donec nec justo eget felis facilisis fermentum. Aliquam 
            porttitor mauris sit amet orci. Aenean dignissim pellentesque felis. Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod 
            in, pharetra a, ultricies in, diam. Sed arcu. Cras consequat."""
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=message_body, fail_silently=False)
            messages.success(request, 'Votre message a bien été envoyé, merci de nous avoir contacter')
            return HttpResponseRedirect('/contact')
    
    form = ContactForm
    
    return render(request, 'pages/contact.html', {'form':form})

def my_account(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)

    return render(request, 'pages/my-account.html', {'profile':profile})

@csrf_exempt
def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, 'vous etes connecté')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors )
            return HttpResponseRedirect('/signup')
    else:
        form = SignupForm()
    data = {'form':form}
    return render(request, 'pages/signup.html', data)



@csrf_exempt
def login_in(request):
    if request.method=='POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # current_user = request.user
            # userprofile = UserProfile.objects.get(user_id = current_user.id)
            # request.session['userimage'] = userprofile.image.url
            messages.success(request, 'Vous etes bien conecté')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, 'Erreur de connection')
            return HttpResponseRedirect('/log_in')

    return render(request, 'pages/loginForm.html')

def login_out(request):
    logout(request)
    return HttpResponseRedirect('/')

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
                    messages.success(request, 'Aucun Article ne correspond a ce nom ')
            else:
                return HttpResponseRedirect('/search/')

    return render(request, 'pages/search.html')
           
    
def first_api(request):
    a = Produit.objects.filter(status=True)
    data={
        'message':'ca marche',
        'articles': [{
            'id': i.id,
            'titre': i.titre,
            'slug': i.slug,
            'image': i.image.url,
        } for i in a]
    }
    return JsonResponse( data, safe=False)
            










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

