from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'phone', 'county', 'sub_county')
   list_filter = ['county', 'sub_county']

   def delete_selected(self, request, queryset):
      empty_name_customers = queryset.filter(name='')
      empty_name_customers.delete()
      self.message_user(request, f"{empty_name_customers.count()} customers with empty names deleted.")

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'date_ordered', 'complete', 'transaction_id', 'get_cart_total', 'get_cart_items']
    list_filter = ['customer']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'product', 'order', 'quantity', 'date_ordered', 'get_total']
    list_filter = ['order__customer']

    def customer_name(self, obj):
        order = obj.order
        if order and order.customer:
            return order.customer.name
        return "N/A"

    customer_name.short_description = 'Customer Name'

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('customer', 'full_name', 'address', 'city', 'state', 'zipcode', 'country')
    list_filter = ['customer']

    def user(self, obj):
        return obj.customer.name if obj.customer else "N/A"

    user.short_description = 'Customer Name'

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(ShippingAddress, ShippingAddressAdmin)
admin.site.register(Category)
