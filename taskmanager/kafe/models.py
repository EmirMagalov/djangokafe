from django.db import models
from datetime import date
# Create your models here.
from django.utils import timezone
class DishCategory(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории блюд"
        verbose_name_plural = "Категории блюд"
class Table(models.Model): #Столы
    number=models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.number}"

    class Meta:
        verbose_name = "Cтол"
        verbose_name_plural = "Столы"
class Dish(models.Model): #Блюда
    name=models.CharField(max_length=255)
    category=models.ForeignKey(DishCategory,on_delete=models.CASCADE)
    price=models.FloatField()

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
class Order(models.Model): #Заказ
    table=models.ForeignKey(Table,on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')
    date = models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Заказ {self.id} на стол {self.table.number} - Статус {self.get_status_display()}"


class OrderItem(models.Model): #Для нескольких блюд

    order = models.ForeignKey(Order, on_delete=models.CASCADE)


    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)


    quantity = models.PositiveIntegerField(default=1)
    date=models.DateField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.dish.name} - {self.quantity} шт."


class Revenue(models.Model):
    date = models.DateField()  # Дата транзакции
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Общая стоимость
    products = models.TextField()  # Продукты, которые были куплены

    def __str__(self):
        return f"Доход от {self.date} на сумму {self.total_amount}₽"

    class Meta:
        verbose_name = "Выручка"
        verbose_name_plural = "Выручка"