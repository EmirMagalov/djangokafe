from django import template
import kafe.views as views
from kafe.models import *
from collections import defaultdict
register=template.Library()
@register.simple_tag()
def get_orderitems():
    order_dict = defaultdict(list)
    orders = Order.objects.all().order_by("-created_at")  # Сортировка по времени создания заказа
    for order in orders:
        order_items = OrderItem.objects.filter(order=order).order_by("-created_at")  # Оставляем порядок добавления блюд
        order_dict[order.table.number].extend(order_items)
    return dict(order_dict)
@register.simple_tag()
def get_oneorderitems(table_number):
    # if table_number:
    table = Table.objects.get(number=table_number)
    # print(table)
    orders = OrderItem.objects.filter(order__table=table).order_by("-created_at")
    return orders
@register.simple_tag()
def one_order(table_number):
    table=Table.objects.get(number=table_number)
    order=Order.objects.filter(table=table).order_by("-date").first()
    return order
@register.simple_tag()
def get_status():
    return views.status