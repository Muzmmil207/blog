from elasticsearch_dsl import Q

from apps.search.documents import PostDocument
from django.http import HttpResponse
from django.views.generic import ListView


class SearchPost(ListView):
    context_object_name = "posts"
    template_name = "apps/search/search-result.html"
    search_document = PostDocument()

    def get_queryset(self):

        if self.request.GET:
            search = self.request.GET.get("search")
            try:
                q = Q(
                "multi_match",
                query=search,
                fields=["title", "summary", "slug", "category", "tags"],
                fuzziness="auto",
            ) & Q(
                should=[Q("match", is_published=True)]
            )
                return self.search_document.search().query(q)

            except Exception as e:
                return HttpResponse(e, status=500)

        return self.search_document.search()
