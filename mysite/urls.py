"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$','lean.views.index',name='index'),
                       url(r'^admin/', include(admin.site.urls)),
					   url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 'lean.views.category', name='category'),
                       url(r'^dajia/$','lean.views.dajia',name='dajia'),
                       url(r'^register/$','lean.views.register',name='register'),
                       url(r'^blog/(?P<article_content>[\w\-]+)$','lean.views.blog',name='blog'),
                       url(r'^blog/','lean.views.wen',name='wen'),
                       url(r'^try/','lean.views.shi',name='try'),
                       url(r'music/','lean.views.music',name='music'),
                       url(r'qiang/$','lean.views.qiang',name='qiang'),
                       url(r'qiang/fatie/$','lean.views.fatie',name='fatie'),
                       url(r'qiang/shiwu/$','lean.views.shiwu',name='shiwu'),
                       url(r'qiang/biaobai/$','lean.views.biaobai',name='biaobai'),
                       url(r'qiang/tucao/$','lean.views.tucao',name='tucao'),
                       url(r'qiang/huodong/$','lean.views.huodong',name='huodong'),
                       url(r'uparticle/','lean.views.uparticle',name='uparticle'),
                       url(r'^zhubo/$','lean.views.zhubo',name='zhubo'),
                       url(r'^zhubo/chinese/$','lean.views.chinese',name='chinese'),
                       url(r'^zhubo/english/$','lean.views.english',name='english'),
                       url(r'^zhubo/chinese/(?P<zhongreporter_content>[\w\-]+)$','lean.views.zhongwen',name='zhongwen'),
                       url(r'^zhubo/english/(?P<yingreporter_content>[\w\-]+)$','lean.views.yingwen',name='yingwen'),
                       url(r'^jiemu/$','lean.views.jiemu',name='jiemu'),
                       url(r'^jiemu/mon/$','lean.views.mon',name='mon'),
                       url(r'^jiemu/tue/$','lean.views.tue',name='tue'),
                       url(r'^jiemu/wed/$','lean.views.wed',name='wed'),
                       url(r'^jiemu/thu/$','lean.views.thu',name='thu'),
                       url(r'^jiemu/fir/$','lean.views.fir',name='fir'),
                       url(r'^jiemu/mon/(?P<zhouyi_content>[\w\-]+)$','lean.views.yi',name='yi'),
                       url(r'^jiemu/tue/(?P<zhouer_content>[\w\-]+)$','lean.views.er',name='er'),
                       url(r'^jiemu/wed/(?P<zhousan_content>[\w\-]+)$','lean.views.san',name='san'),
                       url(r'^jiemu/thu/(?P<zhousi_content>[\w\-]+)$','lean.views.si',name='si'),
                       url(r'^jiemu/fir/(?P<zhouwu_content>[\w\-]+)$','lean.views.wu',name='wu'),
                       url(r'^guanyu/$','lean.views.guanyu',name='guanyu'),
                       url(r'^jiaru/$','lean.views.jiaru',name='jiaru'),
                       )
