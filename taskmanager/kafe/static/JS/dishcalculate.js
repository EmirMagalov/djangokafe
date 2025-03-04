document.addEventListener("click",e=>{
block=e.target.closest(".dish_card")
value=block.querySelector(".quantity")

if (e.target.dataset.plus ){
    e.preventDefault()
    if (value.value<10){
    value.value=parseInt(value.value)+1
}
}
else if(e.target.dataset.minus ){
    e.preventDefault()
    if (value.value>1){
        value.value=parseInt(value.value)-1
    }


}
})
