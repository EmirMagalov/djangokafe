from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'tables', TableViewSet)
router.register(r'categories', DishCategoryViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'revenue', RevenueViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('',main,name="main"),
    path('revenue/',revenue,name="revenue"),
    path('category/<int:pk>/',category,name='category'),
    path('dish/<int:table_id>/<int:category_id>/',dish,name='dish'),
    path('orders/',orders,name='orders')
]
