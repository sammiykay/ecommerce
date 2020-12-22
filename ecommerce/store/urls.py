from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('product/<int:name_id>/', views.view, name='product/<product_id>/'),
    path('process_order/', views.processOrder, name='process_order'),
    path('update_item/', views.updateItem, name='update_item'),
    path('contact-us/', views.contact, name='contact-us'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name='store/reset_password.html'),
    name ='reset_password'),
    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name='store/reset_password_sent.html'), 
    name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name='store/reset_password_confirm.html'),
    name ='password_reset_confirm'),
    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name='store/reset_password_complete.html'),
    name ='password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html'), name ='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='store/logout.html'), name ='logout'),
]
