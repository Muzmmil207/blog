from ckeditor.fields import RichTextField

from django.db import models
from django.db.models import F
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from utils.models.models_fields import AbstractModel


class Category(AbstractModel):
    """
    Post Category table
    """
    name = models.CharField(
        max_length=100,
        verbose_name=_("category name"),
        help_text=_("format: required, max-100"),
        db_index=True,
        unique=True
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name=_("The category slug to form URL."),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
        unique=True
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class Meta:
        verbose_name = _("post category")
        verbose_name_plural = _("post categories")

    def __str__(self):
        return self.name


class PostTags(AbstractModel):
    """
    Post Tags Table
    """
    name = models.CharField(
        max_length=50,
        verbose_name=_("Tag name"),
        help_text=_("format: required, max-50"),
        db_index=True,
        unique=True
    )
    slug = models.SlugField(
        max_length=150,
        verbose_name=_("The tag slug to form URL."),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
        unique=True
    )

    class Meta:
        verbose_name = _("post tag")
        verbose_name_plural = _("post tags")

    def __str__(self):
        return self.name


class Post(AbstractModel):
    class PublishedManager(models.Manager):
        ''' Custom manager for published posts. '''

        def get_queryset(self):
            return super().get_queryset().filter(is_published=True)
    
    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Custom manager

    title = models.CharField(
        max_length=255,
        verbose_name=_("Post Title"),
        db_index=True,
        unique=True
    )
    meta_title = models.CharField(
        max_length=255,
        verbose_name=_("Meta Title"),
        help_text=_("The meta title to be used for browser title and SEO."),
        unique=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="categories"
    )
    tags = models.ManyToManyField(
        PostTags,
        blank=True,
        related_name="tags"
    )
    slug = models.SlugField(
        max_length=255,
        verbose_name=_("Slug"),
        help_text=_("The post slug to form URL."),
        unique=True
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        help_text=_("It can be used to form the table of content of the parent post of series."),
    )
    summary = models.TextField(
        max_length=1015,
        verbose_name=_("Summary"),
        help_text=_("The summary of the post to mention the key highlights.")
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name=_("Published"),
        help_text=_("It can be used to identify whether the post is publicly available.")
    )
    published_at = models.DateTimeField(
        default=now,
        verbose_name=_("Published At"),
        help_text=_("It stores the date and time at which the post is Published.")
    )
    reading_times = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Reading Times"),
        help_text=_("Increasing positive number to calculate the reading times.") 
    )
    trending = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Trending"),
        help_text=_("Increasing positive number to calculate the reading times.") 
    )
    content = RichTextField()

    @property
    def post_img(self):
        try:
            image = self.images.filter(is_main=True).first()
            img_url = image.image.url
        except:
            img_url = ''
        return img_url

    def __str__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        author = self.author
        author.last_activity =  self.updated_at
        author.save()
        super().save(*args, **kwargs)
    
    def plus_one(self, request):
        if  request.session.get('ids') is None:
            request.session['ids'] = []
        
        if not self.id in request.session['ids']:
            self.reading_times=F("reading_times") + 1
            self.trending=F("trending") + 1
            self.save()
            request.session['ids'].append(self.id) 


class PostImage(models.Model):
    """
    The Post Image table.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png"
    )
    is_main = models.BooleanField(
        default=False,
        verbose_name=_("Main Img"),
        help_text=_("Boolean field determine which image will be the main")
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.post.title


class PostMeta(models.Model):
    """
    The Post Meta Table can be used to store additional information of a post
    including the post banner URL etc.
    """
    post = models.OneToOneField(
        Post,
        on_delete=models.CASCADE,
        unique=True
    )
    key = models.CharField(
        max_length=50,
        verbose_name=_("Key"),
        help_text=_("The key identifying the meta.")
    )
    content = models.TextField(
        verbose_name=_("Key"),
        help_text=_("The column used to store the post data.")
    )

    def __str__(self):
        return self.post.title


class PostComment(models.Model):
    """
    Post Comment Table
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        help_text=_("It can be used to form the table of content of the parent comment of series."),
    )
    name = models.CharField(
        max_length=50,
        verbose_name=_("Name"),
        help_text=_("Person name."),
    )
    email = models.EmailField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("E-mail"),
    )
    comment = models.TextField(
        max_length=500,
        verbose_name=_("Comment"),
        help_text=_("The column used to store the comment data."),
    ) 
    created_at = models.DateTimeField(
        default=now,
        verbose_name=_("Created  At"),
        help_text=_("It stores the date and time at which the comment is created.")
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'{self.comment}'[:30]
