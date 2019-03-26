from django.shortcuts import render,redirect
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    return render(request,'welcome.html')
    
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


   