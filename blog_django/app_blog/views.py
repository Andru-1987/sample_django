from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextCommentForm

# Create your views here.

def landing_page(request):
    return render(request, 'index.html', {} )

def forms(request):
    form = TextCommentForm()
    return render(request,'formulario.html',{"form":form})
