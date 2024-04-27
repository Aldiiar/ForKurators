from django.shortcuts import render
from users.forms import LoginForm


# Create your views here.

def main_page_view(request):
    if request.method == "GET":
        if request.user.is_anonymous:
            context = {
                'form': LoginForm
            }

            return render(request, 'registration/login.html', context=context)

        else:
            return render(request, 'layouts/index.html')