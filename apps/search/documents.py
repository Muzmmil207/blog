from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from apps.dashboard.models import Category, Post


#@registry.register_document
class PostDocument(Document):
    category = fields.ObjectField(
        properties={'name': fields.TextField()}
    )
    tags = fields.ObjectField(
        properties={'name': fields.TextField()}
    )
    class Index:
        name = 'post'

    class Django:
        model = Post
        fields = [
            'title',
            'summary',
            'slug',
        ]
