from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Order, OrderItem, Product, PlacedOrder, Pimage, ProRating
from .forms import AddProductForm, ConfirmOrderForm, PimgForm, RateForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import View 
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q


# Create your views here.

# to show the products on the shop page
def shop(request):
    if request.user.is_authenticated:
        products = Product.objects.all().order_by('-id')
        clothing = Product.objects.filter(category='C').order_by('-id')
        clothing_men = Product.objects.filter(category='C', sub_category='men').order_by('-id')
        clothing_men = Product.objects.filter(category='C', sub_category='men').order_by('-id')
        clothing_women = Product.objects.filter(category='C', sub_category='women').order_by('-id')
        electronics = Product.objects.filter(category='E').order_by('-id')
        groceries = Product.objects.filter(category='G').order_by('-id')
        home_accessories = Product.objects.filter(category='HA').order_by('-id')
        context = {
            'shop': 'active', 
            'products': products, 
            'clothing': clothing, 
            'clothing_men': clothing_men, 
            'clothing_women': clothing_women,
            'electronics': electronics, 
            'groceries': groceries, 
            'home_accessories': home_accessories
            }
        return render(request, 'shop/shop.html', context) 
    else:
        return HttpResponseRedirect('/login/')


# to search a particular product by product name
def search(request):
    if request.user.is_authenticated:
        q = request.GET['q']
        products = Product.objects.filter(
            Q(product_name__icontains=q) | Q(price__icontains=q)).order_by('-id')
        # search_result = [item for item in products if searchMatch(q, item)]
        if len(products) == 0:
            messages.add_message(request, messages.ERROR, 'Nothing to show!')
        context = {'shop': 'active', 'products': products}
        return render(request, 'shop/search.html', context) 
    else:
        return HttpResponseRedirect('/login/')

# to add products on the shop
def add_product(request):
    url = request.META.get('HTTP_REFERER')
    if request.user.is_authenticated:
        img_form = PimgForm()
        if request.method == 'POST':
            add_form = AddProductForm(request.POST)
            files = request.FILES.getlist('image')
            if add_form.is_valid():
                product = add_form.save(commit=False)
                product.user = request.user
                product.save()
                for img in files:
                    img = Pimage.objects.create(product=product, image=img)
                add_form = AddProductForm()
                HttpResponseRedirect(url)
                messages.add_message(request, messages.SUCCESS, 'Product added successfully!')
        else:
            add_form = AddProductForm()
            img_form = PimgForm()
        context = {'addForm': add_form, 'imgForm': img_form}
        return render(request, 'shop/addproduct.html', context)
    else:
        return HttpResponseRedirect('/login/')

# to view the details of a single product
def pro_view(request, id):
    # user = User.objects.get(pk=id)
    product = Product.objects.get(pk=id)
    product_rating = ProRating.objects.filter(product_id=id).order_by('-id')
    similar_prods = Product.objects.filter(category=product.category).exclude(id=id)[:3]
    context = {'product': product, 'similar_products': similar_prods, 'productrating': product_rating}
    return render(request, 'shop/proview.html', context)

# to rate a product on a scale of 1-5 stars
def product_rating(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rating = ProRating()
            rating.user = request.user
            rating.product_id = id
            rating.review = form.cleaned_data['review']
            rating.rate = form.cleaned_data['rate']
            rating.save()
    else:
        form = RateForm()
    return HttpResponseRedirect(url)

# to add items into the cart
def add_to_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# to remove a single item from the cart
def remove(request, id):
    item = get_object_or_404(Product, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)[0]
            if order_item.quantity >= 2:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
        else:
            return redirect('/shop/cart/', id=id)
    else:
        return redirect('/shop/cart/', id=id)
    return redirect('/shop/cart/', id=id)

# to remove all items from the cart
def remove_all(request, id):
    item = get_object_or_404(Product, id=id)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)[0]
            order_item.delete()
        if order_item.quantity <= 1:
            order.delete()
        else:
            return redirect('/shop/cart/', id=id)
    else:
        return redirect('/shop/cart/', id=id)
    return redirect('/shop/cart/', id=id)

    
# to show the products added into cart and placing an order
class Cart(View):
    def get(self, *args, **kwargs):
        form = ConfirmOrderForm()
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                    'cart': order, 'form': form,
                    }
            return render(self.request, 'shop/cart.html', context)
        except ObjectDoesNotExist:
            order = OrderItem.objects.all()
            # messages.add_message(self.request, messages.SUCCESS, 'Product added successfully!)
            context = {
                    'cart': order, 'form': form,
                    }
            return render(self.request, 'shop/cart.html', context)
        
    def post(self, *args, **kwargs):    
        form = ConfirmOrderForm(self.request.POST)
        order = Order.objects.get(user=self.request.user, ordered=False)
        ORDERED_ITEMS = OrderItem.objects.filter(user=self.request.user)
        if form.is_valid():
            contact = form.cleaned_data.get('contact')
            address = form.cleaned_data.get('address')
            address2 = form.cleaned_data.get('address2')
            country = form.cleaned_data.get('country')
            city = form.cleaned_data.get('city')
            zip_code = form.cleaned_data.get('zip_code')
            placed_order = PlacedOrder(
                user=self.request.user,
                contact=contact,
                address=address,
                address2=address2,
                country=country,
                city=city,
                zip_code=zip_code
            )
            placed_order.save()
            order.bill_address = placed_order
            order.ordered = True
            ORDERED_ITEMS.update(ordered=True)
            order.save()
            messages.add_message(self.request, messages.SUCCESS, 'Order placed successfully!')
        return redirect('/shop/cart/')
            
