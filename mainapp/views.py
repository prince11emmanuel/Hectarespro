from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from .forms import ContactForm
from django.contrib import messages
from .models import Blog


# Create your views here.
def loading_view(request):
    return render(request, 'mainapp/loading.html')

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

def contact_view(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'mainapp/contact.html', {'form': form})
# or render success message

    return render(request, 'mainapp/contact.html', {'form': form})

def blog_view(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    
    context = {
        'blog': blog,
        'map_url': blog.get_map_url() if blog.has_location() else None,
    }
    
    return render(request, 'mainapp/blog.html', {'blog': blog})



def blog_list_view(request):
    blogs = Blog.objects.all()
    return render(request, 'mainapp/blog_list.html', {'blogs': blogs})
