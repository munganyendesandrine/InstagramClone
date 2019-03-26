from django.shortcuts import render,redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    picture = Profile.objects.all()
    return render(request,'welcome.html',{"picture": picture})
    
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




   