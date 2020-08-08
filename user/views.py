from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.views.decorators.cache import cache_page


# @login_required
# @cache_page(15*60)
def home(request):

    # Send template
    # html_file = get_template('mail_template.html')
    # html_content = html_file.render()
    # sub = 'Test'
    # from_email = 'personaldummymail@gmail.com'
    # to= ['whopawan@gmail.com', ]
    # msg = EmailMultiAlternatives(subject=sub, from_email=from_email, to=to)
    # msg.attach_alternative(html_content, 'text/html')
    # msg.send()

    # Send text
    # subject = "Test"
    # message = "You have Successfully logged in!"
    # from_email = 'personaldummymail.com'
    # recipient = ['whopawan@gmail.com',]
    # send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient)

    return  render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        message  = request.POST.get('message')

        sub = f'Message from {name} - {email}'
        from_email = 'personaldummymail@gmail.com'
        to = ['whopawan@gmail.com',]
        message = message

        send_mail(subject=sub, message=message, from_email=from_email, recipient_list=to)
        return redirect('home')


    return render(request, 'contact.html')





