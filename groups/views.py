from django.shortcuts import render

# Create your views here.

def main_page_view(request):
    if request.method == "GET":
        return render(request, 'layouts/index.html')