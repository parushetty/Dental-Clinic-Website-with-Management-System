from django.db import models


class Appointment_Request(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(null=True,blank=True)
    service_required = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        choices = (
            ('dentalfillings', 'Dental Fillings'),
            ('root_canal_treatment', 'Root Canal Treatment'),
            ('dental_crown', 'Dental Crown'),
            ('wisdom_tooth_removal', 'Wisdom Tooth Removal'),
            ('aligners/invisible_braces', 'Aligners/Invisible Braces'),
            ('metal/ceramic_braces', 'Metal/Ceramic Braces'),
            ('dental_implants', 'Dental Implants'),
            ('denture', 'Denture'),
            ('teeth_whitening', 'Teeth Whitening'),
            ('mouth_ulcers', 'Mouth Ulcers'),
            ('kids_dentistry', 'Kids Dentistry'),
            ('teeth_cleaning', 'Teeth Cleaning'),
            ('teeth/tooth_removal', 'Teeth/Tooth Removal'),
            ('gum_surgery', 'Gum Surgery'),
            ('ortho', 'Ortho'),
            ('others','Others')))
    location = models.CharField(max_length=15)

    def __str__(self):
        db_table = "appointment_request"
        return self.name
    
    class Meta:
        verbose_name = "Appointment Request"
        verbose_name_plural = "Appointment Requests"




class Upcoming_Appointments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=15)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Upcoming Appointment"
        verbose_name_plural = "Upcoming Appointments"

    