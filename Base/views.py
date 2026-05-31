from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
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

        subject = f"New Portfolio Contact - {name}"

        message = f"""
Name: {name}

Email: {email}

Phone: {number}

Message:
{content}
"""

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            ["kaminiparmar31489@gmail.com"],
            fail_silently=False,
        )

        return redirect('/')

    return render(request, 'home.html')