from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'app/homepage.html', {'title': 'Home Page'})

def estimates(request):
    return render(request, 'app/estimates.html', {'title': 'Estimates'})

def layout_ugd_city(request):
    return render(request, 'app/layout_ugd_city.html', {'title': 'Layout UGD City'})