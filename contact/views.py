from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection
from .forms import ContactForm


# Create your views here.
def contact(request):
    sent = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
            send_mail(
                cd['first_name'], cd['message'], cd.get(
                    'email', 'noreply@example.com'), ['ephremwube@gmail.com'])
            return HttpResponseRedirect('/contact?sent=True')
    else:
        form = ContactForm()
        if 'sent' in request.GET:
            sent = True
    return render(request, 'contact/contact.html', {'form': form, 'sent': sent})
