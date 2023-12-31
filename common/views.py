from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

import common.db
import pandas as pd


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        # print(request.POST.get("username"))
        # print(request.POST.get("password1"))
        # print(request.POST.get("email"))
        # new_data = pd.DataFrame({'studentNumber': request.POST.get("username"),
        #                          'password': request.POST.get("password1"),
        #                          'email': request.POST.get("email"),
        #                          'data': ['']})
        # common.db.dataBase = pd.concat([common.db.dataBase, new_data])
        # print(common.db.dataBase)
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


# def login(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request, 'common/login.html', {'form': form})
#
#     elif request.method == "POST":
#         form = LoginForm(request.POST)
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         if form.is_valid():
#             print(4)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             print(username, password)
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('ccca:main')
#     else:
#         form = LoginForm()
#         pass
#
#     return render(request, 'common/login.html', {'form': form})
