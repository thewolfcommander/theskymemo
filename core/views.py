from django.shortcuts import render, redirect

from .forms import ContactForm


def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.ip_address = '127.0.0.1'
            contact.save()
            return redirect('core:home')
        
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)


def single(request):
    return render(request, 'core/single.html')


def typography(request):
    return render(request, 'core/typography.html')