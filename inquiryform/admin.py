from django.contrib import admin

from inquiryform.models import Inquiries, State, City, InquiryType, Status, Notes

admin.site.register(Inquiries)
admin.site.register(State)
admin.site.register(City)
admin.site.register(InquiryType)
admin.site.register(Status)
admin.site.register(Notes)
