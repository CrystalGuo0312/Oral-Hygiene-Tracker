from django.contrib import admin

from .models import Clinic, Dentist, Patient, Announcement, Stat

# Register your models here.
admin.site.register(Clinic)
admin.site.register(Dentist)
admin.site.register(Patient)
admin.site.register(Announcement)
admin.site.register(Stat)
