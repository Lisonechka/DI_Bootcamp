//Ex 1
let age = prompt('Please enter your age')

if (age < 18) {
    alert("Sorry, you are too young to drive this car. Powering off"); 
} else if (age == 18) {
    alert('Congratulations on your first year of driving. Enjoy the ride!');
} else {
    alert("Powering On. Enjoy the ride!");
}
 //Ex1 Objects
let person = {
    username: "admin",
    password: "1234",
};

let database = [person];
console.log(database);

