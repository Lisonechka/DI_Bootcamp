let arrayWords = [];
arrayWords.push(prompt('Write several words separated by commas'));

function wordsInTheStars(){
    let longestWord = 0;
    for (let i = 0; i < arrayWords.length; i++) {
        if ( arrayWords[i].length > longestWord.length ) {
        longestWord = arrayWords[i];
    }
}
return longestWord;
}

wordsInTheStars()

// wordsInTheStars();

// function longestWord(arr) {
    