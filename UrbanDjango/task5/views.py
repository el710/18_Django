from django.shortcuts import render
from django.http import HttpResponse

from .djforms import UserRegister

# Create your views here.

users = ['Lawrence']

def info_update(username: str, passw: str | None, repassw: str | None, age: int | None):
    adds = {}

    if passw != repassw:
        adds.update({"errors": "Пароли не совпадают"})
    elif age < 18:
        adds.update({"errors": "Вы должны быть старше 18 лет"})
    elif username in users:
        adds.update({"errors": "Пользователь уже существует"})
    else:
        users.append(username)
        adds.update({"welcome": f"Приветствуем, {username}!",
                     "errors": ""
                    })

    return adds



def sign_up_by_html(request):
    info = {'title': "HTML forms"}

    if request.method == 'POST':
        username = request.POST.get("user_name")
        password = request.POST.get("user_password")
        repassword = request.POST.get("user_repassword")
        age = request.POST.get("user_age")

        info.update(info_update(username, password, repassword, int(age)))

    return render(request, "registration_page.html", info)


def sign_up_by_django(request):
    info = {'title': "Django forms"}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['userpass']
            repassword = form.cleaned_data['userrepass']
            age = form.cleaned_data['userage']

            info.update(info_update(username, password, repassword, int(age)))
            
        else:
            info.update({"errors": "Поля заполнены некорректно"})
    else:
        form = UserRegister()
    
    info.update({'form': form})

    return render(request, "UserRegister.html", info)