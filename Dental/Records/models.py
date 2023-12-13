from django.db import models
from datetime import datetime
import random
import string


class Patient_Records(models.Model):
    patient_id = models.CharField(primary_key=True, max_length=20, unique=True, editable=False)
    patient_name = models.CharField(max_length=200)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=(('male', 'Male'),('female','Female')))
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True, null=True)
    
    def formatted_phone_number(self, user=None):
        if user and user.is_authenticated and user.is_superuser:
            return self.phone_number
        else:
            if self.phone_number and len(self.phone_number) >= 4:
                start = self.phone_number[:2]
                end = self.phone_number[-2:]
                middle = 'x' * (len(self.phone_number) - 4)
                return f"{start}{middle}{end}"
            return self.phone_number
        
    def formatted_email(self, user=None):
        if user and user.is_authenticated and user.is_superuser:
            return self.email
        else:
            if self.email and len(self.email) >= 4:
                start = self.email[:3]
                end = self.email[-10:]
                middle = 'x' * (len(self.email) - 13)
                return f"{start}{middle}{end}"
            return self.email
        
    def save(self, *args, **kwargs):
        if not self.patient_id:
            # Generate the patient ID based on your desired logic
            self.patient_id = self.generate_custom_patient_id()
        super(Patient_Records, self).save(*args, **kwargs)

    def generate_custom_patient_id(self):
        date_str = datetime.now().strftime('%Y%m%d')
        random_string = ''.join(random.choice(string.ascii_letters.upper() + string.digits) for _ in range(3))
        return f'PID{date_str}{random_string}'

    def __str__(self):
        return self.patient_name
    

    class Meta():
        verbose_name = "Patient Record"
        verbose_name_plural = "Patient Records"
        
    
    
    
class Treatment_Details(models.Model):
    general_details = models.ForeignKey(Patient_Records, on_delete=models.CASCADE)
    visited_on = models.DateField()
    case_name = models.CharField(
        max_length=250,
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
    xray_taken = models.BooleanField(default=False, verbose_name= 'X-Ray Taken')
    opg_taken = models.BooleanField(default=False, verbose_name= 'OPG Taken')
    opg_images = models.ImageField(upload_to='opgimages/', blank=True, null=True)
    case_status = models.CharField(
        max_length=200,
        choices = (
            ('completed','Completed'),
            ('in_progress','In Progress'),
            ('hold','Hold')))
    payment_method = models.CharField(
        max_length=200,
        choices = (
            ('via_UPI','via UPI'),
            ('cash','Cash'),
            ('none','None')))
    payment_status = models.CharField(
        max_length=200,
        choices = (
            ('paid','Paid'),
            ('unpaid','Unpaid'),
            ('none','None')))

    def __str__(self):
        return self.case_name
    

    class Meta:
        verbose_name = "Treatment Details"
        verbose_name_plural = "Treatment Details"