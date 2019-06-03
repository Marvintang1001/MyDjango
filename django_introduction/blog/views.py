from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from  django.core.paginator import Paginator
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
    page = request.GET.get('page')  #请求这个参数
    if page :    #转化成int型数据，如果请求没有附带这个参数，默认置为1
        page = int(page)
    else:
        page = 1
    print('page param: ',page)

    all_article = Article.objects.all()
    top5_article_list = Article.objects.order_by('-publish_date')[:5]

    paginator = Paginator(all_article, 4)
    page_num = paginator.num_pages
    print('page num:',paginator.num_pages)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page+1
    else:
        next_page = page
    if page_article_list.has_previous():
        previous = page-1
    else:
        previous = page


 #   all_article = Article.objects.all()     #取出所有文章
    return render(request, 'blog/index.html',        #render：把模板系统和数据进行渲染和返回
                  {
                      'article_list' : page_article_list,    #字典
                      'page_num' : range(1, page_num+1 ),
                      'curr_page': page,
                      'next_page': next_page,
                      'previous': previous,
                      'top5_article_list': top5_article_list,
                  }
                  )


def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    curr_article = None
    previous_index = 0  #int 用0来初始化
    next_index = 0
    previous_article = None     #变量用None来初始化
    next_article = None
    for index , article in enumerate(all_article):      #迭代
        if index == 0:
            previous_index=0
            next_index = index+1
        elif index == len(all_article) -1:
            next_index=index
            previous_index=index-1
        else:
            previous_index=index-1
            next_index=index+1

        if article.article_id == article_id:
            curr_article = article
            previous_article = all_article[previous_index]
            next_article = all_article[next_index]
            break


    section_list = curr_article.content.split('\n')     #文章内容按空行切分开（按跨行符切分成一个列表）
    return render(request, 'blog/detail.html',        #render：把模板系统和数据进行渲染和返回到 blog/detail.html
                  {
                      'curr_article' : curr_article,    #字典，传入标题到detail.html
                      'section_list' : section_list,    #把它作为变量传入模板系统里，传分段内容
                      'previous_article': previous_article ,
                      'next_article': next_article ,
                  }
                  )
