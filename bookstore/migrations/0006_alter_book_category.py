# Generated by Django 4.1.5 on 2023-01-25 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0005_remove_order_tags_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('science', 'science'), ('fiction', 'fiction'), ('fantasy', 'fantasy'), ('comic', 'comic')], max_length=100, null=True),
        ),
    ]
