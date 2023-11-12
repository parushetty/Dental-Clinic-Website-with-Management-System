from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import AppointmentForm, CustomLoginForm
from django.contrib.auth.views import LoginView


def index(request):
    return render(request,'Appointments/index.html')


def appointment_form(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            location = form.cleaned_data['location']
            
            # Compose the email subject and message
            subject = 'New Appointment Request'
            message = f"Dear Doctor,\n\n     I write this email to inform you that my name is {name} and I would like to bring to your attention that, I have been suffering from dental problems.\n     So, I request you to book an appointment under my name at the earliest.\n\n\nMy Contact Details:\n\n  name: {name}\n  Email: {email}\n  phone Number: {phone_number}\n  location: {location}\n"
        
            # Send the email
            send_mail(subject, message, {email}, ['paruraja24812@gmail.com'])
            # Replace 'from_email@example.com' with your desired sender email address
            # Replace 'recipient@example.com' with the recipient's email address

            form.save()


            # Add further processing or redirect to a success page
            return redirect('appointment_success.html')
    else:
        form = AppointmentForm()
    return render(request, 'Appointments/appointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'Appointments/appointment_success.html')



def dental_tourism(request):
    return render(request, 'Appointments/DENTAL TOURISM.html')



class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm



