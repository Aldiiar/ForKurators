from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm, ChangeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Kurator

def register_view(request):
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
                if not User.objects.filter(username=email).exists():
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
                    print('Пользователь с таким email уже зарегистрирован')
                    form.add_error('email', 'Пользователь с таким email уже зарегистрирован')
            else:
                print('Пароли не совпадают')
                form.add_error('confirm_password', 'Пароли не совпадают')
    else:
        form = RegistrationForm()

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

            return render(request, 'registration/login.html', context=context)
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


def change_profile_view(request):
    user = request.user
    kurator = get_object_or_404(Kurator, user=user)

    if request.method == 'GET':
        if request.user.is_anonymous:
            context = {
                'form': LoginForm
            }
            return render(request, 'registration/login.html', context=context)
        else:
            user_form = ChangeForm(initial={
                'photo': kurator.photo,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'department': kurator.department,
                'university': kurator.university,
                'phone_number': kurator.phone_number,
                'address': kurator.address,
            })
            context = {
                'form': user_form,
            }
            return render(request, 'users/profile_change.html', context=context)

    if request.method == 'POST':
        user_form = ChangeForm(request.POST, request.FILES)

        if user_form.is_valid():
            user.username = user_form.cleaned_data['email']
            user.email = user_form.cleaned_data['email']
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.save()

            kurator.photo = request.FILES.get('photo') or kurator.photo
            kurator.department = user_form.cleaned_data['department']
            kurator.university = user_form.cleaned_data['university']
            kurator.phone_number = user_form.cleaned_data['phone_number']
            kurator.address = user_form.cleaned_data['address']
            kurator.save()

            return redirect('/users/profile/')

        context = {
            'form': user_form,
        }
        return render(request, 'users/profile_change.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('users:login')