# tasks/views.py
from django.shortcuts import render
from .models import Email, Order
from .tasks import send_email_task
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.cache import cache
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
def send_email_view(request):
    if request.method == "POST":
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        email = Email.objects.create(recipient=recipient, subject=subject, body=body)
        send_email_task.delay(email.id)

        return render(request, 'email_sent.html', {'email': email})

    return render(request, 'send_email.html')
from django.shortcuts import render
def order_list(request):
    orders = cache.get('orders_list')

    if not orders:
        orders = Order.objects.select_related('user') \
            .prefetch_related('items') \
            .all()


        cache.set('orders_list', orders, timeout=60*15)

    return render(request, 'tasks/order_list.html', {'orders': orders})
def order_list(request):

    orders = cache.get(f'orders_list_{request.user.id}')

    if not orders:
        orders = Order.objects.select_related('user') \
            .prefetch_related('items') \
            .filter(user=request.user)
        cache.set(f'orders_list_{request.user.id}', orders, timeout=60*15)

    return render(request, 'tasks/order_list.html', {'orders': orders})