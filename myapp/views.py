from django.shortcuts import render, redirect
from myapp.models import Message, ServicePhotos, OurServicesPhotos
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
        subject = f"Ultron Arts New Message From {name}"

        send_mail(
            subject=f'New Message from {name}',
            message=f'Subject: {subject}\n\nMessage:\n{message}\n\nFrom: {name}, Email: {email}',
            from_email='noreply@yourdomain.com',
            recipient_list=['ultronarts77@gmail.com'], 
            fail_silently=False,
        )
   
    data={}
    get_images = ServicePhotos.objects.all()
    data['images'] = get_images

    get_ourServicesImages = OurServicesPhotos.objects.all()
    data['services_photos'] = get_ourServicesImages

    return render(request, "home.html", context=data)

def privacy(request):
    return render(request, "privacy_policy.html")

def adminLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
     
        user = authenticate(username=username, password=password)
        if user is None:
            print("No user found")
            messages.error(request, "Invalid credentials")
        else:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("/site-admin-rupali")
    return render(request, "login.html")


def adminPanel(request):
    data = {}
    if(request.user.is_authenticated):
        if request.method == "POST":
            image = request.FILES.get('image')
            category = request.POST.get('category')
            if(image == None):
                messages.error(request, "Please enter the Image")
            else:
                print(f"The image name is = {image} The Category name is = {category}")
                images_upload = ServicePhotos.objects.create(photo=image, category=category)
                messages.success(request, "Image added to your website")
        get_images = ServicePhotos.objects.all()
        data['images'] = get_images
        print(request.user)

    else:
        return redirect("/admin-rupali-login")
    return render(request, "adminpanel.html", context=data)

def adminServiceImages(request):
    if(request.user.is_authenticated):
        data={}
        if(request.method == "POST"):
            image = request.FILES.get('image')
            name = request.POST.get('name')
            description = request.POST.get('description')
            if(image == None):
                messages.error(request, "Please enter the Image")
            else:
                save_images = OurServicesPhotos.objects.create(photo=image, name=name, description=description)
                messages.success(request, "Image Uploaded")
        get_images = OurServicesPhotos.objects.all()
        data['images'] = get_images
        print(request.user)

    return render(request, "services_images.html", context=data)


def deleteImage(request, id):
    
    image_delete = ServicePhotos.objects.get(id=id)
    image_delete.delete()
    messages.error(request, "Image deleted from your website")
    return redirect('/site-admin-rupali')

def deleteImageFromOurServices(request, id):
    
    image_delete = OurServicesPhotos.objects.get(id=id)
    image_delete.delete()
    messages.error(request, "Image deleted from your website")
    return redirect('/service-images')

def adminMessages(request):
    if(request.user.is_authenticated):

        data={}
        get_message = Message.objects.all()
        data['customerMessages'] = get_message
    else:
        return redirect('/')
    return render(request, "messages.html", context=data)


def deleteMessages(request, id):
    mess_delete = Message.objects.get(id=id)
    mess_delete.delete()
    return redirect('/admin-messages')

def adminLogout(request):
    logout(request)
    messages.error(request, "Logged out")
    return redirect("/admin-rupali-login")

