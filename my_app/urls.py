from django.urls import path
from my_app.views import contact_view,login_view,products_view

urlpatterns = [

    path('contact/',contact_view,name = 'contact'),
    path('login/',login_view,name = 'login'),
    path('products/',products_view,name = 'products'),


]