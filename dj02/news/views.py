from news.models import News_post
from django.shortcuts import render

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})