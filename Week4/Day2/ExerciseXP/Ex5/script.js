let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

function checkBasket() {
    let item = prompt('Wtite an item');
    if (item in amazonBasket) {
        alert(item + ' is in the basket');

    } else {
        alert(item + ' is not in the basket');
    }

}

checkBasket();
