from django.contrib import admin

from inquiryform.models import Inquiries, State, City, InquiryType

admin.site.register(Inquiries)
admin.site.register(State)
admin.site.register(City)
admin.site.register(InquiryType)