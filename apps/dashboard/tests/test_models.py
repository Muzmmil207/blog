import pytest

from apps.authors.models import Author
from apps.dashboard.models import Category, Post


@pytest.mark.parametrize(
    "id, name, slug",
    [
        (1, "django", "django"),
    ],
)
def test_category_db(db, db_fixture_setup, id, name, slug):
    cat = Category.objects.get(id=id)
    assert cat.name == name
    assert cat.slug == slug
    assert str(cat) == name


@pytest.mark.category_db
@pytest.mark.parametrize(
    "name, slug",
    [
        ("fashion", "fashion"),
        ("trainers", "trainers"),
        ("baseball", "baseball"),
    ],
)
def test_category_insert_data(db, category_factory, name, slug):
    cat = category_factory.create(name=name, slug=slug)
    assert cat.name == name
    assert cat.slug == slug
    assert str(cat) == name


@pytest.mark.posts_db
@pytest.mark.parametrize(
    "id, author, created_at, updated_at, title, meta_title, category, slug, parent, summary, is_published, published_at, reading_times, trending, content, tags",
    [
        (
            1,
            1,
            "2022-11-13 22:14:18",
            "2022-11-14 19:34:43",
            "Frist Post",
            "Frist Post",
            1,
            "frist-post",
            None,
            "orem ipsum dolor sit, amet consectetur adipisicing elit. Ratione officia sed, suscipit distinctio, numquam omnis quo fuga ipsam quis inventore voluptatum recusandae culpa, unde doloribus saepe labore alias voluptate expedita? Dicta delectus beatae explicabo odio voluptatibus quas, saepe qui aperiam autem obcaecati, illo et! Incidunt voluptas culpa neque repellat sint, accusamus beatae, cumque autem tempore quisquam quam eligendi harum debitis.",
            1,
            "2022-11-13 22:14:18",
            213,
            0,
            "<p>Sunt reprehenderit, hic vel optio odit est dolore, distinctio iure itaque enim pariatur ducimus. Rerum soluta, perspiciatis voluptatum cupiditate praesentium repellendus quas expedita exercitationem tempora aliquam quaerat in eligendi adipisci harum non omnis reprehenderit quidem beatae modi. Ea fugiat enim libero, ipsam dicta explicabo nihil, tempore, nulla repellendus eos necessitatibus eligendi corporis cum? Eaque harum, eligendi itaque numquam aliquam soluta.</p>\r\n\r\n<p>Explicabo perspiciatis, laborum provident voluptates illum in nulla consectetur atque quaerat excepturi quisquam, veniam velit ex pariatur quos consequuntur? Excepturi reiciendis perferendis, cupiditate dolorem eos illum amet. Beatae voluptates nemo esse ratione voluptate, nesciunt fugit magnam veritatis voluptas dignissimos doloribus maiores? Aliquam, dolores natus exercitationem corrupti blanditiis, consequuntur nihil nobis sed voluptatibus maiores sunt, illo provident aliquid laborum. Vitae, ut.</p>\r\n\r\n<p>Reprehenderit aut sed doloribus blanditiis, aspernatur magni? In molestia<span class=\"marker\">s rem, similique u</span>t esse repudiandae quod recusandae dolores neque earum omnis at, suscipit fuga? Minima qui veniam deserunt quisquam error amet at ratione nesciunt porro quis placeat repudiandae voluptatibus officiis fuga necessitatibus, expedita officia adipisci eaque labore accusamus? Nesciunt repellat illo exercitationem facilis similique quaerat, quis sequi? Praesentium <strong>nulla ipsam dolor.</strong></p>\r\n\r\n<p><strong>Dolorum, incidunt! Ad</strong>ipisci harum itaque maxi<s>me dolores doloremque porro eligendi quis, doloribus vel sit rerum sunt obcaecati nam suscipit nulla vitae alias blanditiis aliquam debitis atque illo modi et placeat. Ratione iure eveniet provident. Culpa laboriosam sed ad quia. Corrupti, earum, perferendis dolore cupiditate sint nihil maiores iusto tempora nobis porr</s>o itaque est. Ut laborum culpa assumenda pariatur et perferendis?</p>\r\n\r\n<p>Est soluta veritatis laboriosam, consequuntur temporibus asperiores, fugit id a ullam sed, expedita sequi doloribus fugiat. Odio et necessitatibus enim nam, iste reprehenderit cupiditate omnis ut iure aliquid obcaecati, repellendus nemo provident eveniet tempora minus! Voluptates aut laboriosam, maiores nihil accusantium, a dolorum quaerat tenetur illo eum culpa cum laudantium sunt doloremque modi possimus magni? Perferendis cum repudiandae corrupti porro.</p>",
            [
                1, 2, 3
            ]
        ),
    ],
)
def test_post_db(
    db, db_fixture_setup,
    id, author, created_at, updated_at,
    title, meta_title, category, slug, parent,
    summary, is_published, published_at, reading_times,
    trending, content, tags
):
    post = Post.objects.get(id=id)
    author = Author.objects.get(id=author)
    cat = Category.objects.get(id=category)
  
    assert str(post) == title
    assert post.author == author
    assert post.meta_title == meta_title
    assert post.category == cat
    assert post.slug == slug
    assert post.tags.all().count() == 3
    assert post.reading_times == 213
    assert post.trending == 0


def test_post_model(db, post_factory, author_factory):

    post_factory.create()
    assert Post.published.count() == 1

