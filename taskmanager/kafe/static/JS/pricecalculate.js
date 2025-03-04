var block = document.querySelectorAll(".orders");

block.forEach(f1 => {
    var n = 0;
    var block_dish = f1.querySelectorAll(".dish_order_block");
    console.log(block_dish)
    block_dish.forEach(f2 => {
        var quantity = parseInt(f2.querySelector(".quantity_orders").value);
        var price = parseFloat(f2.querySelector(".price").innerText.replace(',', '.'));
        var totalDishPrice = price * quantity;

        // Выводим цену для каждого блюда
        f2.querySelector(".price").innerText = totalDishPrice.toFixed(2);
        n += price * quantity;
    });

    f1.querySelector(".totalprice").innerText = n.toFixed(2);
});

