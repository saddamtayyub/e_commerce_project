from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse_lazy

# Create your views here.


def blog_content(request):
    content = Post.objects.all()
    comments = Comment.objects.all()
    for x in comments:
        print(x.body)
    print(request.user.id, 'yoyo')
    return render(request, 'blog.html', {'content': content, 'comment': comments})


def blog_delete(request, id):
    if request.user.is_authenticated:
        fm = Post.objects.get(id=id)
        fm.delete()
        return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/login/')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    print("hello login")
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
            return render(request, 'loginpage.html', {'fm': fm})
    else:
        return HttpResponseRedirect('/home/')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/login/')


def user_profile_page(request):
    if request.user.is_authenticated:
        print(request.user)
        content = Post.objects.filter(user=request.user)
        # for x in content:
        #     print(x.author)
        print(content)
        for x in content:
            print(x.post_author)
            print(x.post_title)
            print(x.post_content)
            print(x.post_image)
        return render(request, 'userpage.html', {'content': content, 'user': request.user})
    else:
        return HttpResponseRedirect('/home/')


def create_blog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            print(request.POST.get('post_title'))
            print("RAN")
            # fm = PostForm(request.POST)
            # if fm.is_valid():
            #     fm.save()
            #     messages.success(request, 'Blog added successfully')
            author = request.POST.get('post_author')
            title = request.POST.get('post_title')
            content = request.POST.get('post_content')
            image = request.FILES.get('image')
            Post.objects.create(
                user=request.user,
                post_author=author,
                post_title=title,
                post_content=content,
                post_image=image,
            )
            return HttpResponseRedirect('/profile/')
        else:
            fm = PostForm()
            return render(request, 'createblog.html', {'fm': fm})
    else:
        return HttpResponseRedirect('/home/')


def edit_blog(request, id):
    if request.user.is_authenticated:
        usr = Post.objects.get(id=id)
        if request.method == "POST":
            # fm = PostForm(request.POST)
            # if fm.is_valid():
            #     fm.save()
            #     messages.success(request, 'Blog added successfully')

            form = PostForm(request.POST, instance=usr)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/profile/')
        else:
            fm = PostForm(instance=usr)
            return render(request, 'createblog.html', {'fm': fm})
    else:
        return HttpResponseRedirect('/home/')


def like_view(request, pk):
    if request.method == "POST":
        id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        print("saved")
        return HttpResponseRedirect('/home/')

    else:
        return HttpResponseRedirect('/home/')


def single_blog(request, pk):
    if request.user.is_authenticated:
        blog = Post.objects.get(id=pk)
        print(blog.id)
        comment = Comment.objects.filter(post=blog)
        for x in comment:
            print(x.body, '-----------comment body')

        return render(request, 'singleblog.html', {'content': blog, 'comment': comment})
    else:
        return HttpResponseRedirect('/home/')


def add_comment(request, pk):
    if request.method == "POST":
        blog = Post.objects.get(id=pk)
        body = request.POST.get('body')
        Comment.objects.create(
            post=blog,
            name=request.user,
            body=body,
        )
        return redirect(reverse_lazy('single_blog', args=[pk]))
    else:
        return HttpResponseRedirect('/home/')


def add_reply(request, post_pk, comment_pk):
    # print(post_pk)
    # print(comment_pk)
    # print("upper")
    post = Post.objects.get(id=post_pk)
    # print(post.post_content)
    parent_comment = Comment.objects.get(id=comment_pk)
    body = request.POST.get('body')
    # print(parent_comment.body)
    Comment.objects.create(
        post=post,
        name=request.user,
        body=body,
        parent=parent_comment,
    )
    return redirect(reverse_lazy('single_blog', args=[post_pk]))


def search_results(request):
    try:
        search = request.POST.get('searched')
        results = Post.objects.filter(post_title__contains=search)
        print(search)
        return render(request, 'results.html', {'search': search, 'results': results})
    except:
        search = ''
        results = ''
        return render(request, 'results.html', {'search': search, 'results': results})
