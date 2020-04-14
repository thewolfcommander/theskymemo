from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    return render(request, 'core/contact.html')


def single(request):
    return render(request, 'core/single.html')


def typography(request):
    return render(request, 'core/typography.html')