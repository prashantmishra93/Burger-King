from django.shortcuts import render
from .models import BurgerDetails, ContactDetail, AboutImage
from .models import Customer, MasterData, MenuCustomer, MenuCustomer2, MenuCustomer3, ContactData


# Create your views here.

def index(request):

##--------------------------Burger Dtail--------------##

    dest = Customer.objects.all()

###--------------------- End Burger Detail---------------------------

##--------------------------Snaks Dtail--------------##

    dest2 = MenuCustomer2.objects.all()

###--------------------- End Snaks Detail---------------------------

##--------------------------Snaks Dtail--------------##

    dest3 = MenuCustomer3.objects.all()

###--------------------- End Snaks Detail---------------------------

##---------------------- Start Master Chef --------------------------

    master = MasterData.objects.all()

##---------------------- End Master Chef --------------------------

##---------------------- Start Contact Us -------------------------

    condet = ContactData.objects.all()

##---------------------- End Contact Us ---------------------------

##---------------------- About Us ---------------------------------

    aboutimg = AboutImage()
    aboutimg.about='about.jpg'


    return render(request, 'index.html', {'dests':dest, 'dests2':dest2, 'dests3':dest3, 'master':master, 'con':condet, 'abouts':aboutimg})

def about(request):
##---------------------- Start Contact Us --------------------------

    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'


    aboutimg = AboutImage()
    aboutimg.about = 'about.jpg'

    return render(request, 'about.html', {'con':condet, 'abouts':aboutimg})

def feature(request):
##---------------------- Start Contact Us --------------------------

    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

    return render(request, 'feature.html', {'con':condet})

def team(request):

##---------------------- Start Contact Us --------------------------
    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

##---------------------- Start Master Chef --------------------------

    master = MasterData.objects.all()

    return render(request, 'team.html', {'con':condet, 'master':master})

def menu(request):

##---------------------- Start Contact Us --------------------------
    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

##--------------------------Burger Dtail--------------##

    ico = MenuCustomer.objects.all()

##-------------------------- End Burger Dtail---------##

##--------------------------Snack Dtail---------------##

    ico2 = MenuCustomer2.objects.all()

##----------------------End Snack Dtail---------------##

##------------------------bevrage Dtail---------------##

    dest1 = BurgerDetails()
    dest1.name = 'Single Cup Brew'
    dest1.desc = 'prashant mishra dolar site amet elit.'
    dest1.price = 7.00
    dest1.img = 'menu-beverage.jpg'
    dest1.specialoffer = True

    dest2 = BurgerDetails()
    dest2.name = 'Caffe Americano'
    dest2.desc = 'prashant mishra dolar site amet elit.'
    dest2.price = 9.00
    dest2.img = 'menu-beverage.jpg'
    dest2.specialoffer = True

    dest3 = BurgerDetails()
    dest3.name = 'Caramel Macchiato'
    dest3.desc = 'prashant mishra dolar site amet elit.'
    dest3.price = 15.00
    dest3.img = 'menu-beverage.jpg'
    dest3.specialoffer = True


    dest4 = BurgerDetails()
    dest4.name = 'Standard black coffee'
    dest4.desc = 'prashant mishra dolar site amet elit.'
    dest4.price = 8.00
    dest4.img = 'menu-beverage.jpg'
    dest4.specialoffer = True


    dest5 = BurgerDetails()
    dest5.name = 'Standard black coffee'
    dest5.desc = 'prashant mishra dolar site amet elit.'
    dest5.price = 12.00
    dest5.img = 'menu-beverage.jpg'
    dest5.specialoffer = True

    ico3 = [dest1, dest2, dest3, dest4, dest5]

##--------------------End bevrage Dtail---------------##

    return render(request, 'menu.html', {'con':condet, 'ico':ico, 'ico2':ico2, 'ico3':ico3})

def book(request):

##---------------------- Start Contact Us --------------------------
    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

##--------------------------Burger Dtail--------------##

    ico = MenuCustomer.objects.all()

##-------------------------- End Burger Dtail---------##

##--------------------------Snack Dtail---------------##

    ico2 = MenuCustomer2.objects.all()

##----------------------End Snack Dtail---------------##

##------------------------bevrage Dtail---------------##

    ico3 = MenuCustomer3.objects.all()

##--------------------End bevrage Dtail---------------##

    return render(request, 'booking.html', {'con':condet, 'ico':ico, 'ico2':ico2, 'ico3':ico3})

def blog(request):

##---------------------- Start Contact Us --------------------------
    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

    return render(request, 'blog.html', {'con':condet})

def detail(request):

##---------------------- Start Contact Us --------------------------
    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

    return render(request, 'single.html', {'con':condet})

def contact(request):

##---------------------- Start Contact Us --------------------------
    condet = ContactDetail()
    condet.address='Kapoorthala Street, Lucknow UP, IND'
    condet.call=7387326099
    condet.email='info@example.com'

    return render(request, 'contact.html', {'con':condet})

def register(request):

    condet = ContactDetail()
    condet.address = 'Kapoorthala Street, Lucknow UP, IND'
    condet.call = 7387326099
    condet.email = 'info@example.com'

    return render(request, 'register.html', {'con':condet})