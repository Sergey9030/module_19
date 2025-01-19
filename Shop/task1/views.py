from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game, News
from datetime import datetime

# Create your views here.
def main_index(request):
    return render(request, 'fourth_task/main_page.html')

def second_index(request):
    games = Game.objects.all()
    context = {'games': games,}
    return render(request, 'fourth_task/second_page.html', context)

def third_index(request):
    return render(request, 'fourth_task/third_page.html')

def sign_up_by_html(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password != repeat_password:
            info = {'head': 'html ', 'error': 'Пароли не совпадают'}
            return render(request, 'fifth_task/registration_page.html', context=info)
        if int(age) < 18:
            info = {'head': 'html ', 'error': 'Вы должны быть старше 18'}
            return render(request, 'fifth_task/registration_page.html', context=info)
        buyer = Buyer.objects.filter(name=username)
        if len(buyer) > 0:
            info = {'head': 'html ', 'error': f'Пользователь {username} уже существует'}
            return render(request, 'fifth_task/registration_page.html', context=info)

        Buyer.objects.create(name=username, age=age, balance=0)
        return HttpResponse(f'{username}, Вы успешно прошли регистрацию. <p><a href="/">На главную</a></p> ')
    info = {'head': 'html ', 'error': ''}
    return render(request, 'fifth_task/registration_page.html', context=info)

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info = {'head': 'html ', 'error': 'Пароли не совпадают'}
                return render(request, 'fifth_task/registration_page.html', context=info)
            if int(age) < 18:
                info = {'head': 'html ', 'error': 'Вы должны быть старше 18'}
                return render(request, 'fifth_task/registration_page.html', context=info)

            buyer = Buyer.objects.filter(name=username)
            if len(buyer) > 0:
                info = {'head': 'html ', 'error': f'Пользователь {username} уже существует'}
                return render(request, 'fifth_task/registration_page.html', context=info)
            Buyer.objects.create(name=username, age=age, balance=0)
            return HttpResponse(f'{username}, Вы успешно прошли регистрацию. <p><a href="/">На главную</a></p> ')
    else:
        form = UserRegister()
        info = {'form': form, 'head': 'Django ', 'error': ''}
        return render(request, 'fifth_task/registration_page.html', context=info)

def news_index(request):
    news = News.objects.all()
    if len(news) == 0:
        for i in range(30):
            t = f'Заголовок{i+1}'
            c = f'Содержимое{i + 1}'
            News.objects.create(title=t, content=c)
        news = News.objects.all()
    paginator = Paginator(news, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'news': page_obj}
    return render(request, 'news.html', context)



