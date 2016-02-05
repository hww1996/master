#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django import forms
from lean.models import Page
from lean.models import Category
from lean.models import User
from lean.models import Article
from lean.models import Music
from lean.models import Qiang
from lean.models import UpArticle
from lean.models import Reporters
from lean.models import Program
from lean.forms import MusicForm
from lean.forms import QiangForm
from lean.forms import UpArticleForm

def index(request):
    category_list = Category.objects.order_by('-age')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'index.html', context_dict)


def category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        pass
    return render(request, 'category.html', context_dict)

def dajia(request):
    return render(request,'dajia.html')

#这是文件上传的views
class UserForm(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})

#这是后台文章
def blog(request,article_content):
    context_dict={}
    try:
        article=Article.objects.get(title=article_content)
        context_dict['article_content']= article.content
        context_dict['article']=article
    except Article.DoesNotExist:
        pass
    return render(request, 'blog.html', context_dict)

#文章区views
def wen(request):
    article=Article.objects.all()
    return render_to_response('wenzhang.html',{'article':article})

def shi(request):
    article=Article.objects.all()
    return render_to_response('try.html',{'article':article})

#这是音乐上传的views
def music(request):
    if request.method == 'POST':
        form =MusicForm(request.POST)
        if form.is_valid():
            music_info = form.save()
            music_info.save()
            return HttpResponse('音乐信息上传成功')
    else:
        form = MusicForm()
    return render(request, 'music.html', {'form_info': form})

#墙区的views
def fatie(request):
    if request.method == 'POST':
        form =QiangForm(request.POST)
        if form.is_valid():
            qiang_info = form.save()
            qiang_info.save()
            return HttpResponse('墙上传成功')
    else:
        form =QiangForm()
    return render(request, 'fatie.html', {'form_info': form})


def detail(request,qiang_id):
    qiang=Qiang.objects.get(id=qiang_id)
    return render_to_response('detail.html',{'qiang_detail':qiang})


def qiang(request):
    qiang=Qiang.objects.all()
    return render_to_response('qiang.html',{'qiang':qiang})

def shiwu(request):
    qiang=Qiang.objects.filter(name='失物')
    return render_to_response('qiang.html',{'qiang':qiang})

def tucao(request):
    qiang=Qiang.objects.filter(name='吐槽')
    return render_to_response('qiang.html',{'qiang':qiang})

def biaobai(request):
    qiang=Qiang.objects.filter(name='表白')
    return render_to_response('qiang.html',{'qiang':qiang})

def huodong(request):
    qiang=Qiang.objects.filter(name='活动')
    return render_to_response('qiang.html',{'qiang':qiang})

#文章投稿
def uparticle(request):
    if request.method == 'POST':
        form =UpArticleForm(request.POST)
        if form.is_valid():
            uparticle_info = form.save()
            uparticle_info.save()
            return HttpResponse('文章上传成功')
    else:
        form = UpArticleForm()
    return render(request, 'uparticle.html', {'form_info': form})

#主播
def reporter(request,reporter_content):
    context_dict={}
    try:
        reporter=Reporters.objects.get(name=reporter_content)
        context_dict['reporter_content']= reporter.content
        context_dict['reporter_partner']=reporter.partner
        program=reporter.program_set.all()
        context_dict['reporter_program']=program
    except Reporters.DoesNotExist:
        pass
    return render(request, 'reporter.html', context_dict)

#主播总览
def zhubo(request):
    zhongreporter=Reporters.objects.filter(category='中文主播')
    yingreporter=Reporters.objects.filter(category='英文主播')
    return render_to_response('zhubo.html',{'zhongreporter':zhongreporter,'yingreporter':yingreporter})
#中文
def chinese(request):
    zhongreporter=Reporters.objects.filter(category='中文主播')
    return render_to_response('chinese.html',{'zhongreporter':zhongreporter})
#英文
def english(request):
    yingreporter=Reporters.objects.filter(category='英文主播')
    return render_to_response('english.html',{'yingreporter':yingreporter})

#节目
def jiemu(request):
    return render(request,'jiemu.html')
#周一
def mon(request):
    zhouyi=Program.objects.filter(category='周一')
    return render_to_response('zhouyi.html',{'zhouyi':zhouyi})
#周二
def tue(request):
    zhouer=Program.objects.filter(category='周二')
    return render_to_response('zhouer.html',{'zhouer':zhouer})
#周三
def wed(request):
    zhousan=Program.objects.filter(category='周三')
    return render_to_response('zhousan.html',{'zhousan':zhousan})
#周四
def thu(request):
    zhousi=Program.objects.filter(category='周四')
    return render_to_response('zhousi.html',{'zhousi':zhousi})
#周五
def fir(request):
    zhouwu=Program.objects.filter(category='周五')
    return render_to_response('zhouwu.html',{'zhouwu':zhouwu})
#节目后台
def program(request,program_content):
    context_dict={}
    try:
        program=Program.objects.get(title=program_content)
        context_dict['program_content']= program.content
        context_dict['program_reporter1']=program.reporter1
        context_dict['program_reporter2']=program.reporter2
    except Program.DoesNotExist:
        pass
    return render(request, 'program.html', context_dict)

#加入我们
def jiaru(request):
    return render(request,'jiaru.html')
#关于
def guanyu(request):
    return render(request,'guanyu.html')