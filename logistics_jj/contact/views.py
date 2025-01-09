from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from .forms import ContactForm
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            name = request.POST['name']
            email = request.POST['email']
            content = request.POST['content']
        try:
            email_message = EmailMessage(
                subject=f'Contact Form from {name}',
                body=content,
                from_email=email,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],)
            email_message.send(fail_silently=False),

            messages.success(request, 'El mensaje se ha enviado correctamente. ¡Gracias por contactarnos!')
        except Exception as e:
            messages.error(request, 'Hubo un error al enviar el mensaje. Por favor, inténtalo nuevamente.')

        return redirect('contact')
    else:
        form = ContactForm()

    context = {'form': form, }
    return render(request, 'contact/contact.html', context)
