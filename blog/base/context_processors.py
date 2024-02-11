from django.shortcuts import get_object_or_404
from base.models import Category, Post
def category(request):
    # Get the Category object based on the provided category_name
    category = Category.objects.all()
    context = {
        "categories": category,
    }
    return context


def popular_trending_latest(request):
    
    latest_posts = Post.objects.all().order_by('-created_on')[:6]

    return {
        "latest_posts": latest_posts,
    }
