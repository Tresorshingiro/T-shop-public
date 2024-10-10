from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('aproduct/<int:product_id>/', views.aproduct, name='aproduct'),
    path('bproduct/<int:product_id>/', views.bproduct, name='bproduct'),
    path('cproduct/<int:product_id>/', views.cproduct, name='cproduct'),
    path('dproduct/<int:product_id>/', views.dproduct, name='dproduct'),
    path('eproduct/<int:product_id>/', views.eproduct, name='eproduct'),
    path('fproduct/<int:product_id>/', views.fproduct, name='fproduct'),
    path('gproduct/<int:product_id>/', views.gproduct, name='gproduct'),
    path('hproduct/<int:product_id>/', views.hproduct, name='hproduct'),
    path('iproduct/<int:product_id>/', views.iproduct, name='iproduct'),
    path('cart', views.cart, name='cart'),
    path('Login/<int:product_id>/', views.Login, name='Login'),
    path('shoe1/<int:product_id>/', views.shoe1, name='shoe1'),
    path('shoe2/<int:product_id>/', views.shoe2, name='shoe2'),
    path('shoe3/<int:product_id>/', views.shoe3, name='shoe3'),
    path('shoe4/<int:product_id>/', views.shoe4, name='shoe4'),
    path('shoe5/<int:product_id>/', views.shoe5, name='shoe5'),
    path('shoe6/<int:product_id>/', views.shoe6, name='shoe6'),
    path('shoe7/<int:product_id>/', views.shoe7, name='shoe7'),
    path('shoe8/<int:product_id>/', views.shoe8, name='shoe8'),
    path('shoe9/<int:product_id>/', views.shoe9, name='shoe9'),
    path('products/<int:product_id>/', views.product_list, name='product_list'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('protected/', views.protected_view, name='protected_view'),
    # Create similar URL patterns for other views...
]
