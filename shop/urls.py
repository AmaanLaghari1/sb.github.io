from django.urls import path, include
from .views import (
    shop,
    search,
    add_product,
    pro_view,
    add_to_cart,
    Cart,
    remove,
    remove_all,
    product_rating
    # increase_quantity
)
from user_profile import views

urlpatterns = [
    path('', shop, name='shop'),
    path('search/', search, name='search'),
    path('add/', add_product, name='addproduct'),
    path('product_details/<int:id>', pro_view, name='productview'),
    path('rate-product/<int:id>', product_rating, name='product_rating'),
    path('add-to-cart/<int:id>', add_to_cart, name='addtocart'),
    # path('increase-quantity/<int:id>', increase_quantity, name='increase_quantity'),
    path('cart/', Cart.as_view(), name='cart'),
    path('remove/<int:id>', remove, name='remove'),
    path('remove-all/<int:id>', remove_all, name='remove_all'),
    #user_profile
    path('profile/<int:id>', views.profile, name='profile'),
    path('changepass/', views.change_pass, name='changepass'),
    path('<int:id>/', views.dlt, name='deleteproduct'),
]