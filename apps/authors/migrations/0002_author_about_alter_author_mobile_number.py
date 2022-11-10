# Generated by Django 4.1.2 on 2022-11-08 17:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authors", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="about",
            field=models.TextField(
                blank=True,
                help_text="Description about the author",
                max_length=1500,
                null=True,
                verbose_name="About",
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="mobile_number",
            field=models.CharField(
                max_length=20,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be entered in the format: `+24901XXXXXXXX`.",
                        regex="^(?:\\+249|0)?(01\\d{8})$",
                    )
                ],
                verbose_name="Mobile Number",
            ),
        ),
    ]
