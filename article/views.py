from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
# Create your views here.


def index(request):
    queryset = Article.objects.all()
    print(queryset)
    context = {
        'queryset': queryset,
    }
    return render(request, 'index.html', context)