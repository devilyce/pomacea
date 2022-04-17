from django.db import models
from django.urls import reverse


class InquiryType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Inquiries(models.Model):
    date_added = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    mobile_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(max_length=300, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    inquiry_type = models.ForeignKey(InquiryType, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, default=1, on_delete=models.SET_DEFAULT)

    def get_absolute_url(self):
        return reverse('inquiry_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.first_name + ' ' + self.last_name
