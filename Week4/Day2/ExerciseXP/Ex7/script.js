let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange',  'apple'];

function checkItemInTheStock (shoppingList) {
    for (let i = 0; i < stock.length; i++ ) {
        for ( let j = 0; j < shoppingList.length; j++) {
        if( i === j) {
            return true;
        }
    }
}
return false
}
checkItemInTheStock(shoppingList);


// function myBill() {

// }
    