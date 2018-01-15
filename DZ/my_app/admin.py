from django.contrib import admin
from.models import *

# Register your models here.


class CreatorsAdmin(admin.ModelAdmin):
    fields = ('creator_name', 'creator_cnt')
    list_filter = ('creator_name', 'creator_cnt')
    list_display = ('creator_name', 'creator_cnt')
    search_fields = ('creator_name', 'creator_cnt')
    list_per_page = 10



class VcardsAdmin(admin.ModelAdmin):
    fields = ('id_card', 'card_name','card_creator','photo','card_price')
    list_filter = ('id_card', 'card_name','card_creator','photo','card_price')
    list_display = ('id_card', 'card_name','card_creator','photo','card_price')
    search_fields = ('id_card', 'card_name','card_creator','photo','card_price')
    list_per_page = 10


class OrdersAdmin(admin.ModelAdmin):
    fields = ('code_order', 'card_order')
    list_filter = ('code_order', 'card_order')
    list_display = ('code_order',)
    search_fields = ('code_order', 'card_order')
    list_per_page = 10


class HumansAdmin(admin.ModelAdmin):
    fields = ('id_human', 'fio', 'order_code')
    list_filter = ('id_human', 'fio', 'order_code')
    list_display = ('order_code')
    search_fields = ('id_human', 'fio', 'order_code')
    list_per_page = 10



admin.site.register(Vcard)
admin.site.register(Creator, CreatorsAdmin)
admin.site.register(Human)
#admin.site.register(Human, HumansAdmin)
admin.site.register(Order, OrdersAdmin)