from django.shortcuts import render
from .models import Question,User
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from zheyes.handle import *

# Create your views here.
@csrf_exempt
def index(request):
    Qlist = Question.objects.all().order_by('-likes')
    query=getPage(request,Qlist)
    index_content=getIndexPage(query)
    # if request.session['client']:
    #     client = request.session['client']
    #     client.username = 'haha'
    session = request.session
    if session.get('client'):
        client = session['client']
        # print(session['client'])
        # print (type(session['client']))
    return render(request, 'zheyes/index.html', locals())
# def find(request):
# 	context={}
# 	return render(request,'zheyes/find.html',context)
@csrf_exempt
def ask(request):
    if request.method == 'POST':
        client = request.session.get('client', default=None)
        if client:
            q_name = request.POST['question_name']
            q_desc = request.POST['question_description']
            askQuestion(uid=client.id, title=q_name, desc=q_desc)
            return HttpResponse('ok')


@csrf_exempt
def article(request):
    if request.method == 'GET':
        qid = request.GET.get('qid')
        user_id = request.GET.get('user_id')
        comment_text = request.GET.get('comment_text')
        article_id = request.GET.get('article_id')
        if qid:
            ques_article = getArticleCommet(int(qid))
            return render(request, 'zheyes/article_detail.html', locals())
        else:
            saveComment(uid=user_id, content=comment_text, aid=article_id)
            return HttpResponse('ok')
    # return render(request,'zheyes/article_detail.html',locals())


@csrf_exempt
def answer(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        question_id = request.POST['question_id']
        article_content = request.POST['article_content']
        saveArticle(uid=user_id, qid=question_id, content=article_content)
        return HttpResponse('ok')
    else:
        qid = request.GET.get('qid')
        client = request.session.get('client', default=None)
        if qid and client:
            question = Question.objects.get(id=qid)
            article = question.article.filter(user_id=client.id)
        return render(request, 'zheyes/answer.html', locals())

		