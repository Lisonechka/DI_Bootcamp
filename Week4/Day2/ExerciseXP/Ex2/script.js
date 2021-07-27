// let userAge = prompt('What is yor age?');

function checkDriverAge(userAge) {
    if (userAge < 18) {
        alert('Sorry, you are too young to drive this car. Powering off');
    } else if (userAge > 18) {
        alert('You are old enough to drive, Powering On. Enjoy the ride!');
    } else {
        alert('Congratulations on your first year of driving. Enjoy the ride!');
    }
}

checkDriverAge( 18);

