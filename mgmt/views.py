from django.db.models import Q
from django.shortcuts import render

from inquiryform.models import Inquiries


def is_valid_queryparam(param):
    return param != '' and param is not None


def mgmt(request):
    return render(request, 'mgmt/base.html')


def search_results(request):
    qs = Inquiries.objects.all()

    name = request.GET.get('name')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    inquiry_type = request.GET.get('inquiry_type')
    status = request.GET.get('status')

    if is_valid_queryparam(name):
        qs = qs.filter(Q(first_name__icontains=name)
                       | Q(last_name__icontains=name)
                       ).distinct()
    if is_valid_queryparam(date_min):
        qs = qs.filter(date_added__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(date_added__lt=date_max)

    if is_valid_queryparam(inquiry_type) and inquiry_type != 'Choose...':
        qs = qs.filter(categories__name=inquiry_type)

    elif is_valid_queryparam(status) and status != 'Choose...':
        qs = qs.filter(categories__name=status)

    context = {'queryset': qs}

    return render(request, 'mgmt/base.html', context)
