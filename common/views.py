from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from common.forms import UserForm

import common.db
import pandas as pd


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print(request.POST.get("username"))
        print(request.POST.get("password1"))
        print(request.POST.get("email"))
        new_data = pd.DataFrame({'studentNumber': request.POST.get("username"),
                                 'password': request.POST.get("password1"),
                                 'email': request.POST.get("email"),
                                 'data': ['']})
        common.db.dataBase = pd.concat([common.db.dataBase, new_data])
        print(common.db.dataBase)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def login(request, user):
    if request.method == "POST":
        #form = LoginForm(request.POST)
        print(request.POST.get("username"))
    else:
        #form = LoginForm()
        pass

    return render(request, 'common/login.html', {'form': form})
