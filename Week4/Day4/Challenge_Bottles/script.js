

var words = "bottles";
var word = "bottle";
let count = prompt('Write number of bottle from 1 to 99');

function countDownBottles () {
for (let x = 1; x  < count; x++) {
while (count > 0) {
    if (count > 1) {
        console.log(count + " " + words + " of beer on the wall");
        console.log(count + " " + words + " of beer!");
        console.log("Take " + x + " down, pass it around");
    } else {
        console.log(count + " " + word + " of beer on the wall");
        console.log(count + " " + word + " of beer!");
        console.log("Take " + x + " down, pass it around");
    }
count = count - x++
    if (count > 1) {
        console.log(count + " " + words + " of beer on the wall!");
    } else if (count == 1) {
        console.log(count + " " + word + " of beer on the wall!");
    } else {
        console.log("No bottles of beer on the wall");
    }
}
}
}
countDownBottles();
