from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from shop.models import Product
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import update_session_auth_hash
from django.views.generic.base import RedirectView
from django.contrib.messages import constants as msg

# Create your views here.
def profile(request, id):
    user_obj = User.objects.filter(pk=id)
    user_products = Product.objects.filter(user=request.user)
    context = {'user': user_obj, 'profile': 'active', 'added_products': user_products}
    return render(request, 'user_profile/profile.html', context)

def change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect(f'/shop/profile/{request.user.id}')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'user_profile/changepass.html', {'form': form})
    else:
        return redirect('/login/')

def dlt(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Product.objects.get(pk=id, user=request.user)
        form.delete()
    return HttpResponseRedirect(url)