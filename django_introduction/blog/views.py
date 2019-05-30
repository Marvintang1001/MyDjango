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


def get_index_page(request):
    all_article = Article.objects.all()     #取出所有文章
    return render(request, 'blog/index.html',        #render：把模板系统和数据进行渲染和返回
                  {
                      'article_list' : all_article    #字典
                  }
                  )


def get_detail_page(request):
    curr_article = Article.objects.all()[4]
    section_list = curr_article.content.split('\n')     #文章内容按空行切分开（按跨行符切分成一个列表）
    return render(request, 'blog/detail.html',        #render：把模板系统和数据进行渲染和返回
                  {
                      'curr_article' : curr_article,    #字典
                      'section_list' : section_list     #把它作为变量传入模板系统里
                  }
                  )
