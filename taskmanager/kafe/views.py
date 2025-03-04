from django.http import HttpResponseRedirect
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from datetime import date
from collections import defaultdict


from .serializers import TableSerializer, DishCategorySerializer, DishSerializer, OrderSerializer, RevenueSerializer
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from collections import defaultdict
# Create your views here.

def main(request):
        tables=Table.objects.all()
        data={
                "tables":tables
        }

        return render(request, 'kafe/main.html',data)

def category(request,pk):

        table=Table.objects.get(pk=pk)

        category_dish=DishCategory.objects.all()
        data = {
                "table": table,
                "category_dish":category_dish
        }
        # if request.method == 'POST':
        #     order_form = OrderForm(request.POST)
        #     if order_form.is_valid():
        #         # Сохраняем заказ
        #         order = order_form.save()
        #
        #         # Получаем все выбранные блюда из POST данных
        #         for dish_id in request.POST.getlist('dish'):
        #             quantity = request.POST.get('quantity_' + dish_id)
        #             dish = Dish.objects.get(id=dish_id)
        #
        #             # Создаем запись в промежуточной таблице OrderItem
        #             OrderItem.objects.create(
        #                 order=order,
        #                 dish=dish,
        #                 quantity=quantity,
        #
        #
        #             )
        #
        #         return render(request, 'kafe/base.html')
        # else:
        #     order_form = OrderForm()
        #
        # # Получаем все блюда, чтобы отобразить их на форме
        # dishes = Dish.objects.all()
        #
        # return render(request, 'kafe/base.html', {'order_form': order_form, 'dishes': dishes})
        return render(request, 'kafe/category.html',data)

def dish(request,table_id,category_id):
        if request.method == 'POST':
                dish_id=request.POST.get("dish_id")
                quantity = request.POST.get("quantity")
                print(dish_id)
                table = get_object_or_404(Table, pk=table_id)
                dish = get_object_or_404(Dish, id=dish_id)
                order,create=Order.objects.get_or_create(table=table)
                if not create:
                        print("exists")

                order_items,create=OrderItem.objects.get_or_create(
                        order=order,
                        dish=dish,
                        defaults={"quantity": quantity}

                )
                if not create:
                        order_items.quantity += int(quantity)
                        order_items.save()
                return redirect(request.META.get('HTTP_REFERER'))
        table = Table.objects.get(pk=table_id)
        dishs=Dish.objects.filter(category=category_id)
        data={
                "table":table,
                "dishs":dishs
        }
        return render(request, 'kafe/dish.html', data)


status=["В ожидании", "Готово", "Оплачено"]


def orders(request):
    if request.method == 'POST':
        table_number = request.POST.get("table")
        status = request.POST.get("status")

        table = get_object_or_404(Table, number=table_number)
        order = get_object_or_404(Order, table=table)


        for key, quantity_orders in request.POST.items():
            if key.startswith("delete_"):
                dish_id = key.split("_")[-1]
                dish = get_object_or_404(Dish, id=dish_id)
                ori=OrderItem.objects.filter(order=order, dish=dish)
                if ori.count() > 1:  
                    ori.delete()
                else:
                    ori.delete()
                    if order.orderitem_set.count() == 0:
                        order.delete()
                continue
            if key.startswith("quantity_orders_") and quantity_orders.isdigit():
                dish_id = key.split("_")[-1]
                dish = get_object_or_404(Dish, id=dish_id)


                order_item = get_object_or_404(OrderItem, order=order, dish=dish)


                order_item.quantity = int(quantity_orders)
                order_item.save()


        if status == "Оплачено":

            order.status = status
            order.save()


            total_amount = 0
            purchased_items = []


            for order_item in order.orderitem_set.all():
                total_amount += order_item.dish.price * order_item.quantity
                purchased_items.append(f"{order_item.dish.name} ({order_item.quantity} шт.)")


            revenue = Revenue(
                date=date.today(),
                total_amount=total_amount,
                products=", ".join(purchased_items),
            )
            revenue.save()


            order.delete()

        return redirect(request.META.get('HTTP_REFERER'))


def revenue(request):
    order_dict = defaultdict(list)
    revenue=Revenue.objects.all()
    for r in revenue:
        order_dict[r.date].append(r)
    data={
        "revenue":dict(order_dict)
    }
    return render(request,"kafe/revenue.html",data)





class TableViewSet(viewsets.ModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['post'])
    def add_item(self, request, pk=None):
        order = get_object_or_404(Order, pk=pk)
        dish_id = request.data.get("dish_id")
        quantity = int(request.data.get("quantity", 1))

        dish = get_object_or_404(Dish, id=dish_id)
        order_item, created = OrderItem.objects.get_or_create(order=order, dish=dish, defaults={"quantity": quantity})

        if not created:
            order_item.quantity += quantity
            order_item.save()

        return Response({"message": "Товар добавлен в заказ"})


class RevenueViewSet(viewsets.ModelViewSet):
    queryset = Revenue.objects.all()
    serializer_class = RevenueSerializer

    @action(detail=False, methods=['get'])
    def grouped_by_date(self, request):
        order_dict = defaultdict(list)
        revenues = Revenue.objects.all()

        for r in revenues:
            order_dict[r.date].append(RevenueSerializer(r).data)

        return Response(order_dict)