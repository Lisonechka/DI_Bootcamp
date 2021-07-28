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