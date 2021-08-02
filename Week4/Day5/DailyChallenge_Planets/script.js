let planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'];
let colors = ['red', 'blue', 'yellow', 'white', 'orange', 'green', 'pink', 'purple'];
for (let i in planets) {
        let newElement = document.createElement('div');
        newElement.className = "planet";
        newElement.textContent = planets[i];
        for (let j = 0; j < colors.length; j++) {
            newElement.style.backgroundColor = colors[j];
        }
        document.body.firstElementChild.appendChild(newElement); 
} 
//in exercise said about backgroundColor, that need to add a new class to each planet, but I added style. But don't
//understand, why all planets are purple.???

//Bonus





