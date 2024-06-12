from django.urls import path
import agthi.views


urlpatterns = [
    path('',agthi.views.home,name='home'),
    path('home', agthi.views.home, name='home'),
    path('restaurants', agthi.views.restaurants, name='restaurants'),
    path('reservation', agthi.views.reservation, name='reservation'),
    path('contact', agthi.views.contact, name='contact'),
    path('single_product', agthi.views.single_product, name='single_product'),
    path('book_table', agthi.views.book_table, name='book_table'),
    path('contact_cust', agthi.views.contact_cust, name='contact_cust'),
]