from django.shortcuts import render,redirect
from .forms import ProfileForm,ImageForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    picture = Profile.objects.all()
    img = Image.objects.all()
    return render(request,'welcome.html',{"picture": picture,"img": img})
    
@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('welcome')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def my_picture(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()
        return redirect('welcome')

    else:
        form = ImageForm()
    return render(request, 'pictures.html', {"form": form})




   