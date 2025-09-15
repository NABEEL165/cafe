from django.shortcuts import render,redirect
from .forms import *
from .models import *
from .forms import ContactForm 


# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect

# shop/views.py return redirect("adminlogin")






def index(request):
    menus = menu.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()
    menus = menu.objects.all() 
    return render(request, 'index.html', {'form': form, 'menus': menus})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

#///////

def book(request):
    if request.method == "POST":
        TableBooking.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            time=request.POST['time'],
            guests=request.POST['guests']
        )
        return redirect('/')  # Redirect to a success page
    return render(request, 'book.html')


def view(request):
    specialties = Specialty.objects.all()
    return render(request, 'view.html', {'specialties': specialties})


from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')  # Change 'login' to your login URL name
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['user_type'] = 'user'  

            messages.success(request, 'User Login successful!')
            return redirect('index')  
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request,'login.html')

def contact_list(request):
    contacts = contactus.objects.all()
    return render(request, 'admin/usercontact.html', {'contacts': contacts})



def booking_list(request):
    bookings = TableBooking.objects.all()
    return render(request, 'admin/userbooking.html', {'bookings': bookings})
from django.shortcuts import render, redirect, get_object_or_404
def delete_contact(request, id):
    contact = get_object_or_404(contactus, id=id)
    contact.delete()
    return redirect('usercontact')  # Replace with your actual view name

def update_contact(request, id):
    contact = get_object_or_404(contactus, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('usercontact')  # Replace with your actual view name
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact.html', {'form': form})



from django.shortcuts import render, redirect, get_object_or_404
from .models import TableBooking
from .forms import BookingForm

def update_booking(request, id):
    booking = get_object_or_404(TableBooking, id=id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('userbooking')  # Replace with your list view name
    else:
        form = BookingForm(instance=booking)
    return render(request, 'book.html', {'form': form})

def delete_booking(request, id):
    booking = get_object_or_404(TableBooking, id=id)
    booking.delete()
    return redirect('userbooking')  # Replace with your list view name








