from django.shortcuts import render

# Create your views here.
def about_menu(request):
    return render(request, 'about/about_menu.html')