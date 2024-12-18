from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']

            email_message = EmailMessage(
                subject=f'Contact Form from {name}',
                body=content,
                from_email=email,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)
            email_message.send(fail_silently=False),

            return render(request, 'contact/contact_valid.html')
    else:
        form = ContactForm()

    context = {'form': form, }
    return render(request, 'contact/contact.html', context)
