from django.shortcuts import render,redirect
from .forms import ProfileForm,ImageForm,CommentsForm
from django.contrib.auth.decorators import login_required
from .models import Profile,Image,Comments
from django.utils.encoding import force_bytes, force_text
from .email import send_activation_email
from .tokens import account_activation_token
from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    picture = Profile.objects.all()
    img = Image.objects.all()
    commenting=Comments.objects.all()
    postsNumber=Image.objects.all().count()
    # num = len(postsNumber)
    
    print(postsNumber)
    
   
    return render(request,'welcome.html',{"picture": picture,"img": img,"commenting": commenting,"postsNumber": postsNumber})

    
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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for confirming email. Now login to your account')
    else:
        return HttpResponse('Activation link is invalid')

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

@login_required(login_url='/accounts/login/')
def my_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('welcome')

    else:
        form = CommentsForm()
    return render(request, 'comments.html', {"form": form})


# def news_today(request):
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']

#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             send_welcome_email(name,email)

#             HttpResponseRedirect('news_today')
#             #.................
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})


def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                to_email = form.cleaned_data.get('email')
                send_activation_email(user, current_site, to_email)
                return HttpResponse('Confirm your email address to complete registration')
        else:
            form = SignupForm()
    return render(request, 'registration/registration_form.html',{'form':form})