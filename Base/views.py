from django.shortcuts import render, redirect
from .models import Contact


def home(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        content = request.POST.get('content')

        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            content=content
        )

        return redirect('/')

    return render(request, 'home.html')