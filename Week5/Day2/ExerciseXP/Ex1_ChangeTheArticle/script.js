//1
document.getElementsByTagName('p')[3].remove();

//2
let x = document.body.firstElementChild.children[1];
x.addEventListener("click", changeColor); 
function changeColor () {
    x.style.backgroundColor = "blue";
}

//3
let y = document.body.firstElementChild.children[0];
y.style.fontSize = Math.floor(Math.random() * 101);

//4
let j = document.body.firstElementChild.children[2];
j.addEventListener("click", hideFunction);
function hideFunction () {
    j.style.display = 'none';
}

//5
let b = document.getElementById("btn");
let p1 = document.body.getElementsByTagName('p')[0];
let p2 = document.body.getElementsByTagName('p')[1];
let p3 = document.body.getElementsByTagName('p')[2];
b.addEventListener("click", makeBold);
function makeBold () {
    p1.style.fontWeight = 'bold';
    p2.style.fontWeight = 'bold';
    p3.style.fontWeight = 'bold';
}

//6
let submitButton = document.getElementById('submit');
let fname = document.getElementById('fname');
let lname = document.getElementById('lname');
submitButton.addEventListener('click', checkValid);
function checkValid(e) {
    if (fname.value == "" || lname.value == "") {
      alert('fill in the empty field');
      e.preventDefault();
    } else { 
      let t = document.createElement("table");
      t.insertRow(0).insertCell(0).textContent = fname.value + ' ' + lname.value;
      document.querySelector(".usersAnswer").appendChild(t);
    }
    
  }

//why result not appears on the screen
