from django.shortcuts import render, get_object_or_404
from django.views import View
from news.models import News
from landing.pagination import pagination


class NewsView(View):
    def get(self, request):
        news = News.objects.all()

        page_number = request.GET.get('page', 1)
        pag_res = pagination(news, page_number)
        
        context = {
            'news': news,

            'page_object': pag_res['page'],
            'is_paginated': pag_res['is_paginated'],
            'next_url': pag_res['next_url'],
            'prev_url': pag_res['prev_url'],
        }

        return render(request, 'news/news.html', context)


class NewsDetailView(View):
    def get(self, request, news_slug):
        news_item = get_object_or_404(News, slug=news_slug)
        
        context = {
            'news_item': news_item,
        }

        return render(request, 'news/news_detail.html', context)