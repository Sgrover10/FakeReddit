from django.shortcuts import render, redirect
from django.contrib import messages
from Login_Reg_App.models import User
from dashboard.models import Post, Comment

def log_reg(request):
    return render(request, 'log_reg.html')


def register(request):
    if request.method=='GET':
        return redirect('/')
        ##validate the data
    errors=User.objects.validator(request.POST)
    if errors:
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id']=new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/posts')

def login(request):
    if request.method=='GET':
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['pw']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/posts')

def logout(request):
    request.session.clear()
    return redirect('/')
    
def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user=User.objects.get(id=request.session['user_id'])
    context={
        'user': user,
        'all_posts': Post.objects.all()
    }
    return render(request, "dashboard/index.html", context)

def profile(request, poster_id):
    ##get user
    user=User.objects.get(id=poster_id)
    context = {
        'user':User.objects.get(id=poster_id),
        'all_posts': user.posts.all()
    }
    ##render profile page
    return render(request, 'dashboard/profile.html', context)





