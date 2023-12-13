# admin_actions.py

from django.core.management import call_command

def backup_patient_records(modeladmin, request, queryset):
    call_command('dbbackup')
