//Part 1 doesn't work
 let zipCode = prompt('Write your Zip Code');
 let zipLength = (String(zipCode)).length;


 switch (zipCode) {
    case zipLength = 5:
        
    case typeof zipcode === "number":
    //   case zipcode.includes(' ') == false:
    //   case zipcode.indexOf(' ') >=== 0:
    case zipCode.search('') == '-1':
         alert('success');
          break;
     case zipLength > 5:
     case zipLength < 5:
         alert('error');
         break;
      default:
          alert('error');
 }

//Part 2
// let zipCode = prompt('Write your Zip Code');
// let regexp = /^[0-9]{5}$/;
// if (regexp.test(zipCode) == true) {
//     alert('success');
// } else {
//     alert('error');
// }

