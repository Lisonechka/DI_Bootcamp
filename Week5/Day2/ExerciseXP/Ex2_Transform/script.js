// let x = document.querySelectorAll('p');
// x.addEventListener("mouseover", highlight);
// x.addEventListener("mouseout", return_normal); 

function highlight() {
    Array.from(document.getElementsByTagName('strong')).forEach(element => {
        element.style.color = 'blue'});
}

function return_normal() {
    Array.from(document.getElementsByTagName('strong')).forEach(element => {
        element.style.color = 'black'})
}

