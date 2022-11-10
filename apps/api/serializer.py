from rest_framework import serializers

from apps.authors.models import Author
from apps.dashboard.models import Category, Post, PostImage

        # queryset=Author.objects.all(),

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    post_img = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["title", "category", "summary", "published_at", "author", "post_img"]

    def get_post_img(self, obj):
        return self.post_img()


class MediaSerializer(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()

    class Meta:
        model = PostImage
        fields = ["img_url", "alt_text"]
        read_only = True
        editable = False

    def get_img_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.img_url.url)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]



# class ProductInventorySerializer(serializers.ModelSerializer):

#     product= ProductSerializer(many=False, read_only=True)

#     class Meta:
#         model = 
#         fields = [
#             "id",
#             "sku",
#             "store_price",
#             "is_default",
#             "product",
#         ]
#         read_only = True

