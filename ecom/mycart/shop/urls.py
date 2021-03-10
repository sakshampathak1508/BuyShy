from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="shop_home"),
    path('about/', views.about, name="shop_about"),
    path('tracker/', views.tracker, name="shop_tracker"),
    path('contact/', views.contact, name="shop_contact"),
    path('checkout/', views.checkout, name="shop_contact"),
    path('products/<int:myid>', views.products, name="shop_prodview"),
]
