from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import UserRegisterForm
# from store.models import Customer
import base64
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('username')
            encode_usr = base64.b64encode(username.encode())
            # Customer.objects.create(
            #     user=encode_usr,
            #     name=username,
            #     email=email

            #     )
            messages.success(request, f'Account for {username} created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
#    u_form = UserUpdateForm()
#    p_form = ProfileUpdateForm()
#    
#    context = {
#        'u_form':u_form,
#        'u_form':u_form,
#    }
    return render(request, 'users/profile.html',)

def change_password(request):
    print("pass form.....>>>>>><<<<<<<<<......////")
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {form: form})

 