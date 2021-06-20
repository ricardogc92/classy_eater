from django.shortcuts import render, redirect
from .models import  User, Restaurant,Reservation
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if "user_id" not in request.session:
        return redirect('/')
    context={
        'user':User.objects.get(id=request.session['user_id']),
        #'reservations':Reservation.objects.filter(user=request.session['user_id']),

    }
    return render(request, 'dashboard.html', context)

def reserve(request):
    context={
        'restaurants':Restaurant.objects.all()
    }
    return render(request,'reserve.html', context)

def add(request):
    return render(request, 'add.html')

def create(request):
    if request.method=='POST':
        errors=Restaurant.objects.validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/dashboard/add')
        user=User.objects.get(id=request.session['user_id'])
        new_restaurant=Restaurant.objects.create(
            name=request.POST['name'],
            category=request.POST['category'],
            address=request.POST['address'],
            city=request.POST['city'],
            zip_code=request.POST['zip-code'],
            capacity=request.POST['capacity'],
            image=request.POST['image'],
            owner=user
        )
    return redirect('/dashboard')

def view(request,res_id):
    context={
        'restaurant':Restaurant.objects.get(id=res_id)
    }
    return render(request,'view.html', context)

def reservation(request, res_id):
    context={
        'restaurant':Restaurant.objects.get(id=res_id)
    }
    return render(request,'reservation.html', context)

def complete(request, res_id):
    if request.method=='POST':
        restaurant=Restaurant.objects.get(id=res_id)
        user=User.objects.get(id=request.session['user_id'])

        errors=Reservation.objects.validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/dashboard/reserve/res_id')
        Reservation.objects.create(
            user=user,
            restaurant=restaurant,
            guests=request.POST['guests'],
            date=request.POST['date'],
            time=request.POST('time')
        )
        
    
    return redirect('/dashboard')


