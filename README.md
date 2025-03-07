# Django Проект для Управления Заказами в Кафе

## Описание
Этот проект представляет собой систему управления заказами в кафе, разработанную с использованием Django. В системе можно управлять столами, добавлять заказы, редактировать их, удалять, а также просматривать общую выручку за день.

### Функционал:
- Отображение списка столов.
- Добавление, редактирование и удаление заказов для каждого стола.
- Просмотр всех заказов, а также заказов конкретного стола.
- Расчет общей выручки за день.
- Динамический расчет стоимости заказа с помощью JavaScript.

## JavaScript
- Динамический расчет стоимости заказа с помощью JavaScript.
- Динамический поиск заказов
## Установка

1. **Клонируйте репозиторий**
   ```sh
   git clone https://github.com/EmirMagalov/djangokafe.git
   cd taskmanager
   ```

2. **Создайте виртуальное окружение и активируйте его**
   ```sh
   python -m venv venv
   source venv/bin/activate  
  
   ```

3. **Установите зависимости**
   ```sh
   pip install -r requirements.txt
   ```

4. **Примените миграции**
   ```sh
   python manage.py migrate
   ```

5. **Создайте суперпользователя (по желанию)**
   ```sh
   python manage.py createsuperuser
   ```

6. **Запустите сервер**
   ```sh
   python manage.py runserver
   ```

7. **Откройте в браузере**
   ```
   http://127.0.0.1:8000/
   ```

## Структура базы данных

### 1. `DishCategory` (Категории блюд)
   - `name` – название категории.

### 2. `Table` (Столы)
   - `number` – номер стола.

### 3. `Dish` (Блюда)
   - `name` – название блюда.
   - `category` – связь с `DishCategory`.
   - `price` – цена блюда.

### 4. `Order` (Заказы)
   - `table` – связь с `Table`.
   - `status` – статус заказа (в ожидании, готово, оплачено).
   - `date` – дата заказа.
   - `created_at` – время создания.

### 5. `OrderItem` (Позиции в заказе)
   - `order` – связь с `Order`.
   - `dish` – связь с `Dish`.
   - `quantity` – количество блюда.
   - `date` – дата заказа.
   - `created_at` – время создания.

### 6. `Revenue` (Выручка)
   - `date` – дата транзакции.
   - `total_amount` – общая сумма.
   - `products` – список купленных блюд.



 
