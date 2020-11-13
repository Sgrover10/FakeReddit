from django.shortcuts import render, redirect
from django.contrib import messages
from Login_Reg_App.models import User
from dashboard.models import Post, Comment

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user=User.objects.get(id=request.session['user_id'])
    context={
        'user': user,
        'all_posts': Post.objects.all()
    }
    return render(request, 'dashboard/index.html', context)

def create_message(request):
    if request.method=='POST':
        ##validate data
        error=Post.objects.empty_validator(request.POST)
        if error:
            messages.error(request, error)
            return redirect('/posts')
        Post.objects.create(
            subject=request.POST['subject'],
            content=request.POST['content'], 
            poster=User.objects.get(id=request.session['user_id']))
        return redirect('/posts')
    return redirect('/posts')

def create_comment(request, post_id):
    if request.method=='POST':
        poster = User.objects.get(id=request.session['user_id'])
        post = Post.objects.get(id=post_id)
        Comment.objects.create(
            content=request.POST['content'], 
            poster= poster,
            post=post)
        return redirect('/posts')
    return redirect('/')

def edit_mess(request, post_id):
    edit_post = Post.objects.get(id=post_id)
    if request.method=="POST":
        edit_post.subject=request.POST['subject']
        edit_post.content=request.POST['content']
        edit_post.save()
        return redirect(f'/user/{str(edit_post.poster.id)}')
    context={
        'edit_post': Post.objects.get(id=post_id)
    }
    return render(request, 'dashboard/edit.html', context)

def edit_comm(request, comm_id):
    edit_comm= Comment.objects.get(id=comm_id)
    if request.method=="POST":
        edit_comm.content=request.POST['content']
        edit_comm.save()
        return redirect('/posts')
    context={
        'edit_comm': Comment.objects.get(id=comm_id)
    }
    return render(request, 'dashboard/edit.html', context)


def delete_mess(request, post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('/posts')

def delete_comm(request, comm_id):
    Comment.objects.get(id=comm_id).delete()
    return redirect('/posts')

def like(request, post_id):
    if request.method=="POST":
        liked_mess=Post.objects.get(id=post_id)
        user_liking=User.objects.get(id=request.session['user_id'])
        liked_mess.likes.add(user_liking)
        return redirect('/posts')
    return redirect('/posts')
    

def unlike(request, post_id):
    if request.method=="POST":
        unliked_mess=Post.objects.get(id=post_id)
        user_unliking=User.objects.get(id=request.session['user_id'])
        unliked_mess.likes.remove(user_unliking)
        return redirect('/posts')
    return redirect('/posts')

