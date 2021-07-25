let number = prompt('Write a number');
let o = "o";
let nO = 'B' + o.repeat(number) + 'm';
let nOBig = nO.toUpperCase();
if (number < 2) {
      alert('Boom');
   } else if ((number >= 2) && (number %2 !== 0)) {
      alert(nO);
  }  else if ((number >= 2) && (number %2 == 0) && (number %5 !== 0)) {
      alert(nO + '!');
  }  else if ((number %2 !== 0) && (number %5 == 0)) {
      alert(nOBig); // Why doesn't work?
  }  else if ((number %2 == 0) && (number %5 == 0)) {
     alert(nOBig + '!');
  }


// Try SWITCH
//  switch(number) {
//     case number < 2: //1
//         alert('Boom');
//       break;
//     case number >= 2:
//     case number %2 !== 0: //2
//         alert(nO)
//       break;
//     case number >= 2:
//     case number %2 == 0:
//     case number %5 !== 0: //3
//         alert(nO + '!');
//       break;
//     case number %2 !== 0:
//     case number %5 == 0: //4
//         alert(nO.toUpperCase())
//       break;
//     case number %2 == 0:
//     case number %5 == 0:
//         alert(nO.toUpperCase() + '!');
//       break;
//  }