document.querySelectorAll(".revenue").forEach(f1 => {
    let n = 0;
    f1.querySelectorAll(".amount").forEach(f2 => {
        let value = parseFloat(f2.innerText.replace(',', '.'));
            n += value;

    });

    let totalAmountElement = f1.querySelector(".total_amount");
    if (totalAmountElement) {
        totalAmountElement.innerText = n.toFixed(2);
    }
});