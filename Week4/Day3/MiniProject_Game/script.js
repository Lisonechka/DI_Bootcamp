function playTheGame() {
        if (!confirm("Would you like to play the game?")) {
            alert("No problem, Goodbye");
        return;

        }

    let computerNumber = Math.round(Math.floor(Math.random() * 11));
    let userGuessNumber;
    for (var i = 0; i < 3; i++) {
        userGuessNumber = checkValidUserGuessNumber();
         if (!userGuessNumber) return;       
         if (test(userGuessNumber, computerNumber)) return;
    }
    alert("out of chance");
              return;
}


function checkValidUserGuessNumber () {
    let guessNumber = parseInt(prompt("Please, write a number between 0 and 10"));
        if (!guessNumber) {
            alert("Sorry Not a number, Goodbye");
         }
         if (guessNumber > 10 || guessNumber < 0) {
             alert('Sorry it’s not a good number, Goodbye');
             return;
            }
            return guessNumber;
        }


function test(userNumber, computerNumber){
    if (userNumber === computerNumber){
        alert ('WINNER');
        return true;
    }
 if (userNumber > computerNumber){
        alert ('Your number is bigger then the computer’s, guess again');
        return false;
 }
    if (userNumber < computerNumber){
     alert ('Your number is smaller then the computer’s, guess again');
    return false;
     }
}
