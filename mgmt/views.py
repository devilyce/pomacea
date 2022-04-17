from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView

from inquiryform.models import Inquiries, InquiryType, Status


def is_valid_queryparam(param):
    return param != '' and param is not None


def mgmt(request):
    qs_inquiry_type = InquiryType.objects.all()
    qs_status = Status.objects.all()

    context = {'inquiry_type': qs_inquiry_type, 'status': qs_status}

    return render(request, 'mgmt/pages/index.html', context)


def search_results(request):
    qs = Inquiries.objects.all()
    qs_inquiry_type = InquiryType.objects.all()
    qs_status = Status.objects.all()

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
        qs = qs.filter(inquiry_type__name=inquiry_type)

    elif is_valid_queryparam(status) and status != 'Choose...':
        qs = qs.filter(status__name=status)

    context = {'queryset': qs, 'inquiry_type': qs_inquiry_type, 'status': qs_status}

    return render(request, 'mgmt/pages/search_results.html', context)


class InquiryDetail(DetailView):
    model = Inquiries
    template_name = 'mgmt/pages/inquiry_detail.html'
    context_object_name = 'data'
