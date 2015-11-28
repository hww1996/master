#coding:utf-8
from django.contrib import admin
from lean.models import Category, Page
from lean.models import Article
from lean.models import Music
from lean.models import Qiang
from lean.models import UpArticle
from lean.models import Zhongreporter
from lean.models import Yingreporter
from lean.models import Zhouyi
from lean.models import Zhouer
from lean.models import Zhousan
from lean.models import Zhousi
from lean.models import Zhouwu
# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ArticleAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
#音乐
class MusicAdmin(admin.ModelAdmin):
    list_display = ['music_name', 'music_singer','music_number','time']
    list_filter=['time']

#墙区
class QiangAdmin(admin.ModelAdmin):
    list_display = ['title','name', 'author','time']
    list_filter=['name','time']

#文章投稿
class UpArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author','time']
    list_filter=['time']

#主播
#中文主播
class ZhongreporterAdmin(admin.ModelAdmin):
    list_display = ['name']

#英文主播
class YingreporterAdmin(admin.ModelAdmin):
    list_display = ['name']
#节目
#周一
class ZhouyiAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
#周二
class ZhouerAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
#周三
class ZhousanAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
#周四
class ZhousiAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
#周五
class ZhouwuAdimin(admin.ModelAdmin):
    list_disaplay=['title','timestamp']
# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
#文章区
admin.site.register(Article,ArticleAdimin)
#音乐区
admin.site.register(Music, MusicAdmin)
#墙区
admin.site.register(Qiang,QiangAdmin)
#文章投稿区
admin.site.register(UpArticle,UpArticleAdmin)
#中文主播
admin.site.register(Zhongreporter,ZhongreporterAdmin)
#英文主播
admin.site.register(Yingreporter,YingreporterAdmin)
#节目
#周一
admin.site.register(Zhouyi,ZhouyiAdimin)
#周二
admin.site.register(Zhouer,ZhouerAdimin)
#周三
admin.site.register(Zhousan,ZhousanAdimin)
#周四
admin.site.register(Zhousi,ZhousiAdimin)
#周五
admin.site.register(Zhouwu,ZhouwuAdimin)