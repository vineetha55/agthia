from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    return render(request,'tem/home_page.html')


def restaurants(request):
    return render(request,'tem/restaurants.html')


def reservation(request):
    return render(request, 'tem/home_page.html')


def contact(request):
    return render(request, 'tem/contact.html')


def single_product(request):
    return render(request, 'tem/single_product.html')


def book_table(request):
    email = "user09.wahylab@gmail.com"
    nam = request.POST.get('nam')
    emm = request.POST.get('emm')
    count = request.POST.get('count')
    dat = request.POST.get('dat')
    tim = request.POST.get('tim')
    t_a = 'Name: '+nam+', Email: '+emm+', Number of person: '+count+', Date: '+dat+', Time of arrival: '+tim+'.'
    send_mail('Table booking (Agthia)', t_a, email, [email], fail_silently=False)
    return redirect('home')


def contact_cust(request):
    email = "user09.wahylab@gmail.com"
    nam = request.POST.get('nam')
    emm = request.POST.get('emm')
    subj = request.POST.get('subj')
    phone = request.POST.get('phone')
    msg = request.POST.get('msg')
    t_a = 'Name: ' + nam + ', Email: ' + emm + ', Subject: ' + subj + ', Phone: ' + phone + ', Message: ' + msg + '.'
    send_mail('Customer message (Agthia)', t_a, email, [email], fail_silently=False)
    return redirect('home')
