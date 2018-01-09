from django.shortcuts import render
from django.views.generic import View,ListView
from datetime import datetime
from .models import *
# Create your views here.
from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import View, ListView
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

class OrdersView(View):
    def get(self, request):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3}
            ]
        }
        return render(request, 'orders.html', locals())


class OrderView(View):
    def get(self, request, id):
        variable = 'Django'
        today_date = datetime.now()
        data = {
            'order': {
                'id': id
            }
        }
        return render(request, 'order.html', locals())


def main(request):
    return render(request, 'main.html', locals())


def db(request):
    return render(request, 'db.html', locals())


class VcardView(ListView):
    model = Vcard
    template_name = 'cards.html'


class CreatorView(ListView):
    model = Creator
    template_name = 'creators.html'


def card_info(request, id):
    name = ['1060', '1080', 'Titan']
    gtx1060_info = 'Видеокарта GeForce GTX 1060 оснащена инновационными игровыми технологиями, что делает ее идеальном выбором для самых современных игр в высоком разрешении. Видеокарта GeForce GTX 1060 создана на основе архитектуры NVIDIA Pascal™, самой технически продвинутой архитектуры GPU из когда-либо созданных. Она обеспечивает высочайшую производительность, которая открывает дорогу к VR-играм и другим возможностям. '
    gtx1080_info = 'Новый флагманский GPU NVIDIA GeForce GTX 1080 - самая технически продвинутая игровая видеокарта на планете. Откройте для себя непревзойденную производительность, энергоэффективность и игровые возможности благодаря новой архитектуре NVIDIA Pascal™. Это лучшая игровая платформа.'
    Titan_info = 'NVIDIA TITAN Xp – самая мощная в мире видеокарта. Невероятная вычислительная мощность и инновационная архитектура NVIDIA Pascal™ обеспечивают производительность, необходимую для выполнения задач, о которых вы и не мечтали.'
    info = [gtx1060_info, gtx1080_info, Titan_info]
    data1 = {'card': {'id': id}}
    data2 = {'cards': [{'id': '1', 'card_name': 'GEFORCE GTX 1060', 'info': gtx1060_info},
                       {'id': '2', 'card_name': 'GEFORCE GTX 1080 Ti', 'info': gtx1080_info},
                       {'id': '3', 'card_name': 'NVIDIA TITAN Xp', 'info': Titan_info}]}
    return render(request, 'card_info.html', locals())

def registration(request):
    errors = {'username': '', 'password': '', 'password2': '', 'email': '', 'firstname': '', 'surname': ''}
    error_flag = False
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            errors['username'] = 'Введите логин'
            error_flag = True
        elif len(username) < 5:
            errors['username'] = 'Логин должен превышать 5 символов'
            error_flag = True
        elif User.objects.filter(username=username).exists():
            errors['username'] = 'Такой логин уже существует'
            error_flag = True
        password = request.POST.get('password')
        if not password:
            errors['password'] = 'Введите пароль'
            error_flag = True
        elif len(password) < 8:
            errors['password'] = 'Длина пароля должна превышать 8 символов'
        password_repeat = request.POST.get('password2')
        if password != password_repeat:
            errors['password2'] = 'Пароли должны совпадать'
            error_flag = True
        email = request.POST.get('email')
        if not email:
            errors['email'] = 'Введите e-mail'
        firstname = request.POST.get('firstname')
        if not firstname:
            errors['firstname'] = 'Введите имя'
        surname = request.POST.get('surname')
        if not surname:
            errors['surname'] = 'Введите фамилию'
        if not error_flag:
            # ...
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=surname)
            return HttpResponseRedirect('/login/')
    return render(request, 'registration.html', locals())


def login(request):
    error = ""
    username = None
    password = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/success/')
        else:
            error = "Пользователь не найден"
    return render(request, 'login.html', locals())


#@login_required()
def success(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/login/')
    return render(request, 'success.html', locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')


def registration2(request):
    form = RegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get('username'),
                                            email=request.POST.get('email'),
                                            password=request.POST.get('password'),
                                            first_name=request.POST.get('firstname'),
                                            last_name=request.POST.get('surname'))
            # ...
            return HttpResponseRedirect('/login/')
        else:
            form = RegistrationForm()
    return render(request, 'registration2.html', {'form': form})
