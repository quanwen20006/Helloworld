from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Article
from datetime import datetime
from django.shortcuts import redirect


def homepage(request):
    template = get_template('index.html')
    articles = Article.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showarticle(request, slug):
    template = get_template('article.html')

    try:
        article = Article.objects.get(slug=slug)
        if article != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

