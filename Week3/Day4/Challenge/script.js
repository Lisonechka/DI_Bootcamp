let sentence = "The dish is not so bad, I can eat it."
let wordNot = sentence.indexOf('not');
let wordBad = sentence.indexOf('bad');
if(wordBad > wordNot) {
    let newSentence = sentence.replace(/not.*bad/, "good");
    console.log(newSentence);
} else {
    console.log(sentence);

}