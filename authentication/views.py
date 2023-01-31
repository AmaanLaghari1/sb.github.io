from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LogInForm
from django.contrib import messages

# Create your views here.

# def register(request):
#     if not request.user.is_authenticated:
#         form = RegisterForm()
#         form1 = LogInForm()
#         if request.POST.get('submit') == 'sign_up':
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             form = RegisterForm()
#         elif request.POST.get('submit') == 'log_in':
#             form1 = LogInForm(request=request, data=request.POST)
#             if form1.is_valid():
#                 uname = form1.cleaned_data['username']
#                 upass = form1.cleaned_data['password']
#                 user = authenticate(username=uname, password=upass)
#                 if user is not None:
#                     login(request, user)
#                     return redirect('/shop/')
#         else:
#             form = RegisterForm()
#             form1 = LogInForm()
#         return render(request, 'auth.html', {'form': form, 'form1': form1})
    
def signup(request):
    if not request.user.is_authenticated:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Your account has been created successfully!")
        else:
            form = RegisterForm()
        return render(request, 'auth/signup.html', {'form': form, 'signup': 'active'})
    else:
        return HttpResponseRedirect('/shop/')

def userlog(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LogInForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, "You've successfully logged in")
                    return redirect('/shop/')
        else:
            form = LogInForm()
        return render(request, 'auth/login.html', {'form': form, 'login': 'active'})
    else:
        return HttpResponseRedirect('/shop/')


def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/login/')
    