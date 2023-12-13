from django.utils.html import format_html
from django.contrib import admin
from .models import Patient_Records, Treatment_Details
from .forms import TreatmentDetailsForm
from django.http import HttpResponse
from django.conf import settings
import csv



class TreatmentDetailsInline(admin.StackedInline):
    model = Treatment_Details
    form = TreatmentDetailsForm
    extra = 1

    fields = ('visited_on','case_name','xray_taken','opg_taken','opg_images','case_status','payment_method','payment_status')


def export_patient_records_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patient_records.csv"'

    writer = csv.writer(response)
    # Define the header row for the CSV file
    writer.writerow(["Patient ID", "Patient Name","Age","Gender","Location","Phone Number","Email","Visited On","Case Name","X-Ray Taken","OPG Taken","OPG  Images","Case Status","Payment Method","Payment Status"])
    
    for patient_record in queryset:
        for treatment_record in patient_record.treatment_details_set.all():
            # Replace 'ParentModel' and 'InlineModel' with your actual model field names
            opg_images_url = "" 
            if treatment_record.opg_images:
                opg_images_url = request.build_absolute_uri(settings.MEDIA_URL + treatment_record.opg_images.name)

            writer.writerow([
                patient_record.patient_id,
                patient_record.patient_name,
                patient_record.age,
                patient_record.gender,
                patient_record.location,
                patient_record.phone_number,
                patient_record.email,
                treatment_record.visited_on,
                treatment_record.case_name,
                treatment_record.xray_taken,
                treatment_record.opg_taken,
                opg_images_url,
                treatment_record.case_status,
                treatment_record.payment_method,
                treatment_record.payment_status
            ])

    return response

export_patient_records_as_csv.short_description = "Export Parent Records"
   

@admin.register(Patient_Records)
class PatientRecordAdmin(admin.ModelAdmin):
    list_display = ('patient_id','patient_name','age','gender','phonenumber','mail','location','treatment')
    search_fields = ('patient_id','patient_name', 'age','email','location')
    list_filter = ('created_at','treatment_details__case_name', 'treatment_details__case_status', 'treatment_details__payment_method', 'treatment_details__payment_status', 'treatment_details__visited_on')
    actions = [ export_patient_records_as_csv]


    def patient_id(self, obj):
        return obj.patient_id
    patient_id.short_description = 'Patient ID'

    def patient_name(self, obj):
        return obj.patient_name
    patient_name.short_description = 'Patient Name'

    def age(self, obj):
        return obj.age
    age.short_description = 'Age'

    def gender(self, obj):
        return obj.gender
    gender.short_description = 'Gender'

    def location(self, obj):
        return obj.location
    location.short_description = 'Location'


    def phonenumber(self, obj):
        return obj.formatted_phone_number()
    phonenumber.short_description = 'Phone Number' 
    

    def mail(self, obj):
        return obj.formatted_email()
    mail.short_description = 'Email'
    

    def treatment(self, obj):
        treatment_details = obj.treatment_details_set.all()
        treatment_display = ""
        
        for details in treatment_details:
            treatment_display += format_html(
                "<strong>Visited On:</strong> {}<br>"
                "<strong>Case Name:</strong> {}<br>"
                "<strong>Case Status:</strong> {}<br>"
                "<strong>Payment Method:</strong> {}<br>"
                "<strong>Payment Status:</strong> {}<br><br>",
                details.visited_on,
                details.case_name,
                details.case_status,
                details.payment_method,
                details.payment_status,
            )
        
        return format_html(treatment_display)
    
    treatment.short_description = 'Treatment Details'

    inlines=[TreatmentDetailsInline]

