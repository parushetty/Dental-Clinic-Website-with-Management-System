from django.core.management import call_command

def create_backup():
    call_command('dbbackup')
