//Favorite color
let me = ["my","favorite","color","is","blue"]
console.log(me.join(' '))
//or
let me = ["my","favorite","color","is","blue"];
let mejoin = me.join(' ');
console.log(mejoin);

//Mixup
let str1 = "milk";
let str2 = "fresh";
let newStr1 = str2.slice(0, 2) + str1.slice(2);
let newStr2 = str1.slice(0, 2) + str2.slice(2);
let newWord = newStr1+ " " + newStr2;
console.log(newWord);


//Calculator "+"
let num1 = prompt('Enter the first number');
let num2 = prompt('Enter the second number')
let sum = Number(num1) + Number(num2)
alert('The sum is ' + sum);

//Calculator "-"
let num1 = prompt('Enter the first number');
let num2 = prompt('Enter the second number')
let subtract = Number(num1) - Number(num2)
alert('The result is ' + subtract);

//Calculator '*'
let num1 = prompt('Enter the first number');
let num2 = prompt('Enter the second number')
let multiply = Number(num1) * Number(num2)
alert('The result is ' + multiply);

//Calculator "/"
let num1 = prompt('Enter the first number');
let num2 = prompt('Enter the second number')
let divide = Number(num1) / Number(num2)
alert('The result is ' + divide);
