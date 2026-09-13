from django.contrib import admin

from Qpage.models import *

# Register your models here.
admin.site.register(Cart)

admin.site.register(Item)

from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'payment_method', 'payment_status', 'timestamp']
    list_filter = ['payment_status', 'timestamp']
    search_fields = ['user__username', 'payment_method']
    