from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from inquiryform.forms import InquiriesForm, City
from inquiryform.models import Inquiries


def home(request):
    if request.method == 'GET':
        form = InquiriesForm()
    else:
        form = InquiriesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if Inquiries.objects.filter(email=instance.email).exists():
                messages.warning(request, 'email already exist')
            else:
                instance.save()
                messages.success(request, 'success')
                subject = 'subject here'
                from_email = settings.EMAIL_HOST_USER
                to_email = [instance.email]
                body = 'message here'
                send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=body,
                          fail_silently=False)

    return render(request, 'home/pages/index.html', {'form': form})


# AJAX
def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'home/widgets/city_dropdown_list_options.html', {'cities': cities})
