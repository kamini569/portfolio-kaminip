from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact


def home(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message') or request.POST.get('content')

        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            message=message
        )

        subject = f"New Portfolio Contact - {name}"

        email_message = f"""
Name: {name}

Email: {email}

Phone: {number}

Message:
{message}
"""

        try:
            send_mail(
                subject,
                email_message,
                settings.EMAIL_HOST_USER,
                ["kaminiparmar31489@gmail.com"],
                fail_silently=False,
            )
        except Exception as e:
            print("EMAIL ERROR:", e)

        return redirect('/')

    return render(request, 'home.html')