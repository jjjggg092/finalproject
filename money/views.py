from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from money.models import Balance, Sves, Ins, Spends


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    bal = Balance.objects.filter(uname = request.user.username)
    sav = Sves.objects.filter(uname = request.user.username)
    print(Ins.objects.filter(uname = request.user.username))
    context = {
    "user": request.user,
    'balance': bal[0],
    'saves': sav[0],
    'Ins': Ins.objects.filter(uname = request.user.username),
    'Spends': Spends.objects.filter(uname = request.user.username)
    }
    return render(request, "principal/base.html", context)

def signup(request):
    username = request.POST['regusername']
    password = request.POST['regpassword']
    email = request.POST['email']
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return render(request, "users/login.html", {'reg_message': 'Username or email already registered'})
    else:
        user = User.objects.create_user(username, email, password)
        user.first_name = request.POST['regfname']
        user.last_name = request.POST['reglname']
        user.save()
    ba = Balance(uname = username, money = 0.00)
    sa = Sves(uname = username, money = 0.00)
    ba.save()
    sa.save()
    context = {
        'reg_message': "Welcome!!!"
    }
    return render(request, "users/login.html", context)


def login_view(request):
    username = request.POST["logusername"]
    password = request.POST["logpassword"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        print('xdxdxd')
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def addmo(request):
    uname = request.user.username
    type = str(request.POST['type'])
    per = int(request.POST['save'])
    quant = float(request.POST['quanuty'])
    date = str(request.POST['date'])
    mo = Ins(uname=uname, kind=type, save=per, quantity=quant, date=date)
    saved = round(quant*(per/100),2)
    bal = Balance.objects.get(uname = request.user.username)
    bal.money = bal.money + quant - saved
    sav = Sves.objects.get(uname = request.user.username)
    sav.money = saved + sav.money
    bal.save()
    sav.save()
    context = {
        "user": request.user,
        'balance': bal,
        'saves': sav,
        'Ins': Ins.objects.filter(uname = request.user.username),
        'Spends': Spends.objects.filter(uname = request.user.username)
        }
    return render(request, "principal/base.html", context)

def outs(request):
    uname = request.user.username
    type = str(request.POST['wtype'])
    quant = float(request.POST['wquanuty'])
    date = str(request.POST['wdate'])
    mo = Spends(uname=uname, kind=type, quantity=quant, date=date)
    mo.save()
    bal = Balance.objects.get(uname = request.user.username)
    bal.money = bal.money - quant
    sav = Sves.objects.get(uname = request.user.username)

    bal.save()
    context = {
        "user": request.user,
        'balance': bal,
        'saves': sav,
        'Ins': Ins.objects.filter(uname = request.user.username),
        'Spends': Spends.objects.filter(uname = request.user.username)
        }
    return render(request, "principal/base.html", context)
