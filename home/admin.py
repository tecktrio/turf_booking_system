from django.contrib import admin
from .models import Booked_turf, Contact, Turf, Users ,Manager_Requests
# Register your models here.

admin.site.register(Turf)
admin.site.register(Booked_turf)
admin.site.register(Users)
admin.site.register(Manager_Requests)
admin.site.register(Contact )