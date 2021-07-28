
function isDivisible() {
    let result = "";
    let sum = 0;
    for (i =0; i <501; i++) {
        if (i %23 === 0) {
            result += i + " ";
            sum +=i
        }
    }
    console.log(result);
     console.log(sum);
    
 }
 isDivisible()

//Bonus
// function isDivisible(divisor) {
//     let result = "";
//     let sum = 0;
//     for (i =0; i <501; i++) {
//         if (i %divisor === 0) {
//             result += i + " ";
//             sum +=i
//         }
//     }
//     console.log(result + " the numbers divisible by " + divisor + ", and their sum is " + sum);
    
// }
// isDivisible(3);
// isDivisible(45);
