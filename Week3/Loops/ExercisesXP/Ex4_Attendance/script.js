let guestList = {
    randy: "Germany",
    karla: "France",
    wendy: "Japan",
    norman: "England",
    sam: "Argentina"
  }
let student = prompt('What is your name?');
for (let i in guestList) {
    if (i = student) {
        alert("Hi! I\'m " + student + " and I'\m from " + guestList[i] + ".");
    } else {
        alert("Hi! I\'m a guest."); //Why this part doesn't work?
    }
}
