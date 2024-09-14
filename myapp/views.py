from django.shortcuts import render
from myapp.models import Message

# Create your views here.


def home(request):
    if(request.method=="POST"):
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if(name=="" or email=="" or message==""):
            print("Please enter details")
        save_message = Message.objects.create(name=name, email=email, message=message)
        save_message.save()

    return render(request, "home.html")

def privacy(request):
    return render(request, "privacy_policy.html")