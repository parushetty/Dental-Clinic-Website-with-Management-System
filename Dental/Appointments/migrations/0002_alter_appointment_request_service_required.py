# Generated by Django 4.2.5 on 2023-10-13 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment_request',
            name='service_required',
            field=models.CharField(blank=True, choices=[('dentalfillings', 'Dental Fillings'), ('root_canal_treatment', 'Root Canal Treatment'), ('dental_crown', 'Dental Crown'), ('wisdom_tooth_removal', 'Wisdom Tooth Removal'), ('aligners/invisible_braces', 'Aligners/Invisible Braces'), ('metal/ceramic_braces', 'Metal/Ceramic Braces'), ('dental_implants', 'Dental Implants'), ('denture', 'Denture'), ('teeth_whitening', 'Teeth Whitening'), ('mouth_ulcers', 'Mouth Ulcers'), ('kids_dentistry', 'Kids Dentistry'), ('teeth_cleaning', 'Teeth Cleaning'), ('teeth/tooth_removal', 'Teeth/Tooth Removal'), ('gum_surgery', 'Gum Surgery'), ('ortho', 'Ortho'), ('others', 'Others')], max_length=40, null=True),
        ),
    ]
