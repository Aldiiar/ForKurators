from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Kurator

def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegistrationForm()
        }
        return render(request, 'registration/register.html', context=context)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            department = form.cleaned_data['department']
            university = form.cleaned_data['university']
            phone_number = form.cleaned_data['phone_number']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                user = User.objects.create_user(
                    username=email,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=password
                )

                kurator = Kurator.objects.create(
                    user=user,
                    department=department,
                    university=university,
                    phone_number=phone_number,
                    address=address
                )

                return redirect('/users/login/')
            else:
                pass


        context = {
            'form': form
        }
        return render(request, 'registration/register.html', context=context)


def profile_view(request):
    if request.method == 'GET':
        if request.user.is_anonymous:
            context = {
                'form': LoginForm
            }

            return render(request, 'registration/login.html', context=context)  # Перенаправляем анонимного пользователя на страницу входа
        else:
            user = request.user
            return render(request, 'users/profile.html', {'user': user})

def login_view(request):
    if request.method == 'GET':
        context = {
            'form': LoginForm
        }

        return render(request, 'registration/login.html', context=context)

    if request.method =='POST':
        data = request.POST
        form = LoginForm(data=data)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password')
            )

            if user:
                login(request, user)
                return redirect('/users/profile')
            else:
                form.add_error('email', 'пароль и email не совпадают')

        return render(request, 'registration/login.html', context={
            'form': form
        })


def logout_view(request):
    logout(request)
    return redirect('users:login')