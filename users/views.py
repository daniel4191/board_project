from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from .forms import SignupForm, LoginForm
from .models import User

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = SignupForm(data = request.POST, files = request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/posts/")
        
    else:
        form = SignupForm()
        
    context= {"form":form}
    return render(request, "users/signup.html", context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect("/posts/")

    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username = username, password = password)
            
            if user:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, "입력한 정보에 해당하는 유저가 없습니다.")
        
        
    else:
        form = LoginForm()
    
    context = {"form": form}
    return render(request, "users/login.html", context)

def logout_view(request):
    logout(request)
    return redirect("/users/login/")