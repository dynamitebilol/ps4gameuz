
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from games.forms import ReviewForm
from .models import Category, Game, HeroSection, Review

def home(request):
    if request.GET.get('q'):
        games =  Game.objects.filter(title__icontains=request.GET.get('q'))[:10]
    else:
        games = Game.objects.all()[:9]
    categories = Category.objects.all()
    heros = HeroSection.objects.all()
    context = {'games':games, 'categories':categories, 'heros':heros}
    return render(request, 'home.html', context)



def games(request):


    if request.GET.get('q'):
        games =  Game.objects.filter(title__icontains=request.GET.get('q'))
    else:
        games = Game.objects.all()


    page = request.GET.get('page')
    paginator = Paginator(games, 6)

    try:
        games = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        games = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        games = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    categories = Category.objects.all()
    context = {'games':games, 'categories':categories, 'custom_range':custom_range}
    return render(request, 'games.html', context)


def game(request, slug):
    game = Game.objects.get(slug=slug)
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.save()
            return redirect('game', slug=game.slug)

        
    context = {'game':game}
    return render(request, 'single-game.html', context)


def category(request, slug):
    if request.GET.get('q'):
        category_games =  Game.objects.filter(title__icontains=request.GET.get('q'))
    else:
        category_games = Game.objects.filter(category__contains=slug)


    page = request.GET.get('page')
    paginator = Paginator(category_games, 6)

    try:
        category_games = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        category_games = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        category_games = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)


    categories = Category.objects.all()
    context = {'category_games':category_games,'categories':categories, 'custom_range':custom_range, 'slug':slug.upper()}
    return render(request, 'categories.html', context)  