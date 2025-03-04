from rest_framework import serializers
from .models import Table, DishCategory, Dish, Order, OrderItem, Revenue

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class DishCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DishCategory
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    dish = DishSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='orderitem_set', many=True)

    class Meta:
        model = Order
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'
