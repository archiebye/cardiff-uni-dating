from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

from .forms import UserForm, ProfileForm
from .models import Profile

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        #user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)  #user_form.is_valid() and
        if profile_form.is_valid():
            #user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('users')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        #user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/update_profile.html', {
        #'user_form': user_form,
        'profile_form': profile_form
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('update_profile')
    else:
        form = UserCreationForm()
    return render(request, 'signup/signup.html', {'form': form})


def signin(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	
	if user is not None:
		if user.is_active():
			login(request, user)
        
		else:
			return render(request, 'signup/signup.html',{
				'login_message' : 'The user has been removed',})

	else:
		return render(request, 'signin/signin.html',{
			'login_message' : 'Enter the username and password correctly',})
	return HttpResponseRedirect('users')

def userlist(request):
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #return render(request, 'blog/post_list.html', {'posts': posts})
    if request.user.profile.is_male():

        users = Profile.objects.filter(gender__icontains='f')
        return render(request, 'profile/profile.html', {'users': users})

    else:
        users = Profile.objects.filter(gender__icontains='m')
        return render(request, 'profile/profile.html', {'users': users})

@login_required
def signout(request):
		#user = request.user
		logout(request)
		return render(request, 'signout/signout.html')







