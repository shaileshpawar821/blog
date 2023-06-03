from django.shortcuts import render
from .models import Post
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def index(request):
    content={}
    content['data'] = Post.objects.filter(is_published=True)
    return render(request,'core/index.html',content)
#---------------------------------------------
# login_view views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful." )
                return index(request)
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})

#---------------------------------------------
# register_view views here.
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful." )
            return redirect('login_view')
    else:
        form = RegistrationForm()
        messages.error(request, "Unsuccessful registration. Invalid information.")
    return render(request, 'core/register.html', {'form': form})

#---------------------------------------------
# logout_view views here.
def logout_view(request):
    logout(request)
    return index(request)
#---------------------------------------------
# create_post views here.
@login_required(login_url='login_view')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = PostForm()
    return render(request,'core/post_create.html',{'form': form})
#---------------------------------------------
# edit_post views here.
@login_required(login_url='login_view')
def edit_post(request, pk):
    instance = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            form.save()
            return index(request)
    else:
        form = PostForm(instance=instance)
    
    return render(request, 'core/edit_post.html', {'form': form})




    


    