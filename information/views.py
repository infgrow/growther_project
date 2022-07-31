from multiprocessing import context
from django.shortcuts import render
from .models import FaqContent, HowTo

# Create your views here.

def information(request):
    faqs = FaqContent.objects.all()
    how_tos = HowTo.objects.all()
    context = {'faqs': faqs, 'how_tos': how_tos}
    return render(request, 'information/index.html', context=context)

def about(request):
    return render(request, 'information/about.html')