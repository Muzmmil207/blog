from elasticsearch_dsl import Q

from apps.dashboard.models import Post
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .documents import PostDocument


class SearchPost(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "apps/search/search-result.html"
    search_document = PostDocument

    def get_queryset(self):
        if self.request.GET:
            try:
                q = self.request.GET('data')
                
                return self.search_document.search().filter(title=q)

            except Exception as e:
                return HttpResponse(e, status=500)
        return self.search_document.search().filter(title='')
