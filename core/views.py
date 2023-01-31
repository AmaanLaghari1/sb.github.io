from django.shortcuts import render
from django.views.generic import TemplateView
from shop.models import Product
from .forms import ContactForm

# Create your views here.
def home(request):
    featured = Product.objects.order_by('-pub_date')[:5]
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {'home': 'active', 'featured_items': featured, 'conform': form}
    return render(request, 'index.html', context)