from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'User Login Succefull')
            return redirect('adminprofile')  # Change to your admin dashboard URL name
        else:
            messages.error(request, 'Invalid credentials or not an admin user.')
            return redirect('admin/adminlogin')

    return render(request, 'admin/adminlogin.html')


def adminprofile(request):
    return render(request,'admin/adminprofile.html')


def user_contact_view(request):
    return render(request, 'admin/usercontact.html')


