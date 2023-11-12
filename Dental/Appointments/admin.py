from django.utils.html import format_html
from django.contrib import admin
from .models import Appointment_Request, Upcoming_Appointments
from django.http import HttpResponse
from django.conf import settings
import csv


# Register your models here.
def move_records_to_upcoming(modeladmin, request, queryset):
    for record in queryset:
        # Create a new instance of TargetModel with the relevant data
        target_record = Upcoming_Appointments(name=record.name, email=record.email, phone_number=record.phone_number, location=record.location)
        # Save the new record to the TargetModel
        target_record.save()
       # Optionally, you can delete the record from the SourceModel
        record.delete()
move_records_to_upcoming.short_description = "Accept Requests"

@admin.register(Appointment_Request)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','service_required','location')
    actions = [move_records_to_upcoming]

    def has_add_permission(self, request):
        return False



@admin.register(Upcoming_Appointments)
class UpcomingAppointmentsAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone_number','location','date','time')
    #actions = [move_records_to_upcoming_appointments]







