from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Post, Category, Comment, CustomUser
from .forms import MyUserCreationForm, CommentForm
from django.shortcuts import get_object_or_404


def user_login(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)

        try:
            user = CustomUser.objects.get(email=email)
            print("try")
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'email OR password does not exist')
            print('else')

    context = {'page': page}
    return render(request, 'base/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def user_signup(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email'].lower()

            # Check if a user with the same email already exists
            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'Email is already in use.')
                return render(request, 'base/signup.html', {'form': form})

            user = form.save(commit=False)
            user.email = email
            user.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/signup.html', {'form': form})


def index(request):
    posts = Post.objects.all().order_by("-created_on")
    category = Category.objects.all()
    context = {
        "posts": posts,
        "category":category,
    }
    return render(request, 'base/index.html', context)

def about(request):
    context={'name':'Ali'}
    return render(request, 'base/about.html', context)

def contact(request):
    context={'name':'Ali'}
    return render(request, 'base/contact.html', context)


def category(request, category_name):
    # Get the Category object based on the provided category_name
    category = get_object_or_404(Category, name=category_name)

    # Retrieve all posts related to the specified category
    posts = Post.objects.filter(categories=category).order_by("-created_on")

    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, 'base/category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form":CommentForm()
    }

    return render(request, 'base/single-post.html', context)

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  # Set the comment author to the current user
            comment.post = post
            comment.save()
            return redirect('single-post', pk=post_id)
    else:
        form = CommentForm()
        print(form)

    return render(request, 'single-post.html', {'form': form, 'post': post})
