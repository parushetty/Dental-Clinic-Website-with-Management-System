import csv
from django.core.management.base import BaseCommand
from Records.models import Patient_Records, Treatment_Details
from datetime import datetime


class Command(BaseCommand):
    help = 'Import patient records from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                 visited_on = datetime.strptime(row['visited_on'], '%d-%m-%Y').date()

                 patient_id = row['patient_id']
                 existing_record = Patient_Records.objects.filter(patient_id=patient_id).first()
                 
                 if existing_record:
                      existing_record.patient_name = row['patient_name']
                      existing_record.save()
                 else:
                  patient_record = Patient_Records.objects.create(
                      patient_id=row['patient_id'],
                      patient_name=row['patient_name'],
                      age=row['age'],
                      gender=row['gender'],
                      location=row['location'],
                      phone_number=row['phone_number'],
                      email=row['email'],
                     )
                  
                  treatment_detail = Treatment_Details(
                      general_details=patient_record,
                      visited_on=visited_on,
                      case_name=row['case_name'],
                      xray_taken=row['xray_taken'],
                      opg_taken=row['opg_taken'],
                      opg_images=row['opg_images'],  # Assuming you have an ImageField
                      case_status=row['case_status'],
                      payment_method=row['payment_method'],
                      payment_status=row['payment_status'],
                      )
                  treatment_detail.save()


        self.stdout.write(self.style.SUCCESS('Patient records imported successfully.'))
