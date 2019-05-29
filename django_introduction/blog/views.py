from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

def article_content(request):
    article = Article.objects.all()[1]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    return_str = 'title: %s<br /> brief_content: %s<br /> content: %s<br /> article_id: %s<br /> publish_date: %s' %(title,
                                                                                                 brief_content,
                                                                                                 content,
                                                                                                 article_id,
                                                                                                 publish_date)
    return HttpResponse(return_str)
