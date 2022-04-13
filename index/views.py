from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from inquiryform.forms import InquiriesForm, City


def index(request):
    if request.method == 'GET':
        form = InquiriesForm()
    else:
        form = InquiriesForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index/base.html', {'form': form})


# AJAX
def load_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'index/widgets/city_dropdown_list_options.html', {'cities': cities})