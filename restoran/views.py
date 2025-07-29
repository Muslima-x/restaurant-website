from django.shortcuts import render, redirect
from restoran import models
from django.shortcuts import get_object_or_404


def home(request):
    if request.POST:
        full_name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        people=request.POST.get('people')
        special_request=request.POST.get('message')
        peoplee=models.Order.objects.get(people=people)
        models.Book_Online.objects.create(full_name=full_name, email=email, date=date, people=peoplee, special_request=special_request)
        return redirect('home')
    
    filter_category=request.GET.get('filter')
    if filter_category:
        dishes=models.Dishes.objects.filter(category__name=filter_category)
    else:
        dishes=models.Dishes.objects.filter(category__name= 'Breakfast')
        
    categories=models.Category.objects.all()
    main=models.Main.objects.all()
    about=models.About.objects.first()
    home_service=models.Home_Service.objects.filter(is_active=True)
    people = models.Order.objects.all()
    ourteam=models.Ourteam.objects.filter(is_active=True)
    client=models.Clients.objects.filter(is_active=True)
    footer=models.Footer.objects.first()
    context={
        'main':main,
        'about':about,
        'home_service':home_service,
        'people':people,
        'ourteam':ourteam,
        'client':client,
        'footer':footer,
        'dishes':dishes,
        'categories':categories,
    }

    return render(request, 'index.html', context)



def about(request):
    about=models.About.objects.first()
    ourteam=models.Ourteam.objects.all()
    footer=models.Footer.objects.first()
    return render(request, 'about.html', {'about':about, 'ourteam':ourteam,'footer':footer})



def service(request):
    home_service=models.Home_Service.objects.all()
    footer=models.Footer.objects.first()
    return render(request, 'service.html', {'home_service':home_service, 'footer':footer})


def menu(request):
    footer=models.Footer.objects.first()
    filter_category=request.GET.get('filter')
    if filter_category:
        dishes=models.Dishes.objects.filter(category__name=filter_category)
    else:
        dishes=models.Dishes.objects.filter(category__name= 'Breakfast')
    categories=models.Category.objects.all()

    return render(request, 'menu.html', {'categories':categories, 'dishes':dishes, 'footer':footer})



def contact(request):
    footer=models.Footer.objects.first()
    contact_email=models.Contact_Email.objects.first()
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        models.Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, 'contact.html', {'contact_email':contact_email, 'footer':footer})



def booking(request):
    footer=models.Footer.objects.first()
    if request.POST:
        full_name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        people=request.POST.get('people')
        special_request=request.POST.get('message')
        peoplee=models.Order.objects.get(people=people)
        models.Book_Online.objects.create(full_name=full_name, email=email, date=date, people=peoplee, special_request=special_request)
        return redirect('booking')
    
    
    people = models.Order.objects.all()
    return render(request, 'booking.html', {'people':people, 'footer':footer})



def ourteam(request):
    footer=models.Footer.objects.first()
    ourteam=models.Ourteam.objects.all()
    return render(request, 'team.html', {'ourteam':ourteam, 'footer':footer})


def testmonial(request):
    footer=models.Footer.objects.first()
    client=models.Clients.objects.all()
    return render(request, 'testimonial.html', {'client':client, 'footer':footer})


def footer(request):
   footer=models.Footer.objects.first()
   return render(request, 'base.html', {'footer':footer})




# Create your views here.
