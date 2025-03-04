function filterOrders(event) {
    let input = event.target.value.toLowerCase();  // получаем значение из поля ввода
    let orders = event.target.closest('.orderblock').querySelectorAll('.orders');  // получаем все заказы внутри родительского блока

    orders.forEach(order => {
        let dishes = order.querySelectorAll(".dish-name");
        let table = order.querySelector(".table-number");
        let match = false;

        // Поиск по названию блюда
        dishes.forEach(dish => {
            if (dish.textContent.toLowerCase().includes(input)) {
                match = true;
            }
        });

        // Поиск по номеру стола
        if (table && table.textContent.toLowerCase().includes(input)) {
            match = true;
        }

        // Показать или скрыть заказ в зависимости от совпадений
        order.style.display = match ? "block" : "none";
    });
}


document.addEventListener("click", (e) => {
    let form = e.target.closest(".dish_order_block");
    if (!form) return;

    let value = form.querySelector(".quantity_orders");

    if (!value || isNaN(value.value)) {
        value.value = 1; // Устанавливаем значение по умолчанию
    }

    if (e.target.dataset.plus) {
        e.preventDefault();
        if (parseInt(value.value) < 10) {
            value.value = parseInt(value.value) + 1;
        }
    } else if (e.target.dataset.minus) {
        e.preventDefault();
        if (parseInt(value.value) > 1) {
            value.value = parseInt(value.value) - 1;
        }
    }
});
