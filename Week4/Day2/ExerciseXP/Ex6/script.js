// Quarters  = 0.25
// Dimes = 0.10
// Nickels = 0.05
// Pennies = 0.01

function changeInPocket (quarters, dimes, nickels, pennies) {
    let sum = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01);
    console.log(sum);
}

//second function doesn't work
 function changeEnough(sumChangeInPocket, itemPrice) {
     sumChangeInPocket = changeInPocket ();
     if (sumChangeInPocket > itemPrice) {
         return true;
     } else {
         return false;
     }
 }
 changeEnough((2, 100, 0, 0), 14.11);
 changeEnough((0, 0, 20, 5), 0.75)
 