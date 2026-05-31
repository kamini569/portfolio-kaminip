from django.shortcuts import render, redirect
from .models import Contact
import requests

BOT_TOKEN = "8973986453:AAHBx_HI0aA-Xrcx_mF67mFzy5FKSfnRmTo"
CHAT_ID = "5980707306"


def home(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            number=number,
            message=message
        )

        telegram_message = f"""
🔥 New Portfolio Contact

👤 Name: {name}
📧 Email: {email}
📱 Phone: {number}

💬 Message:
{message}
"""

        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={
                    "chat_id": CHAT_ID,
                    "text": telegram_message
                },
                timeout=10
            )
        except Exception as e:
            print("Telegram Error:", e)

        return redirect("/")

    return render(request, "home.html")