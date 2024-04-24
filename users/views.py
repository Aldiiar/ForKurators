from django.shortcuts import render
from users.forms import RegisterForm

def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=context)

def profile_view(request):
    return render(request, 'users/profile.html')