from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
import db


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
        db.dataBase.append(new_data)
        print(db.dataBase)
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
