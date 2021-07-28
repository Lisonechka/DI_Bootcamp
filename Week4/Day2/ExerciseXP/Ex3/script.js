let number = prompt("Write the number");
function checkNumber() {
    for (let i = number; i >= 0 && i <=100; i) {
        if (i %2 === 0) {
            alert('the number ' + [i] + ' is even');
            break;
        } else {
            alert('the number ' + [i] + ' is odd');
            break;
        }
    }
}
checkNumber(number);
