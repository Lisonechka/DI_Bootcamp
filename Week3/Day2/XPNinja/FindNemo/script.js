let sentence = prompt('Write,please, any sentence containing the word Nemo');
let positionOfNemo = sentence.search('Nemo');
if (positionOfNemo >= 0) {
    console.log('I found Nemo at ' + positionOfNemo);
} else {
    console.log('I can’t find Nemo');
}