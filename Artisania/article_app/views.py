from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list_article(request):
    return render(request,'article_app/article.html')