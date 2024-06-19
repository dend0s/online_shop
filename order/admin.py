from django.contrib import admin
from .models import Order, OrderProduct


class ItemInlineOrder(admin.TabularInline):
    model = OrderProduct
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInlineOrder]
    list_display = ['id', 'user', 'phone_number', 'completed']
    fields = ['user', 'first_name', 'last_name', 'city', 'address', 'date', 'delivery', 'pay_method',
              'total_price', 'pay_status', 'completed']
    readonly_fields = ['user', 'date']


admin.site.register(Order, OrderAdmin)
