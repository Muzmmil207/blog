# Generated by Django 4.1.3 on 2022-11-13 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "dashboard",
            "0002_rename_user_category_author_rename_user_post_author_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="reading_times",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Increasing positive number to calculate the reading times.",
                verbose_name="Reading Times",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="trending",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Increasing positive number to calculate the reading times.",
                verbose_name="Trending",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="categories",
                to="dashboard.category",
            ),
        ),
    ]
