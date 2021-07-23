from django.contrib import admin
from .models import Customer, MasterData, MenuCustomer, MenuCustomer2, MenuCustomer3, ContactData

# Register your models here.

admin.site.register(Customer)

admin.site.register(MasterData)

admin.site.register(MenuCustomer)

admin.site.register(MenuCustomer2)

admin.site.register(MenuCustomer3)

admin.site.register(ContactData)