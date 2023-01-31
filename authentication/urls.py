from django.urls import path, include
from core import views
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('', views.Home.as_view(), name='home'),
    # path('', include('authentication.urls')),
    path('logout/', views.log_out, name='logout'),
    path('login/', views.userlog, name='login'),
    path('signup/', views.signup, name='signup'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='auth/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/pass_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/pass_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='auth/pass_reset_complete.html'), name='password_reset_complete'),
]
