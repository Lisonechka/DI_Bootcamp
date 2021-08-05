let listTasks = [];

let addButton = document.getElementById('submit');
let inputTask = document.getElementById('addTask');
addButton.addEventListener('click', addTask);
function addTask(e) {
    e.preventDefault();
    if 
    (inputTask.value == "") {
     alert('fill in the task field');
    } 
    else { 
    listTasks=inputTask.value;
    let ul = document.createElement('ul');//ul
    let li = document.createElement('li');//li
    
    
    let checkbox = document.createElement('input');//checkbox
    checkbox.type = 'checkbox';
    checkbox.name = "name";
    checkbox.value = "value";
    checkbox.id = "id";
    li.textContent = listTasks;

    let buttonX = document.createElement('button');
    buttonX.id = 'buttonX';
    buttonX.textContent = 'X';
    
    
    //doesn't work
    // let icon = document.createElement('i');
    // icon.type = 'button'
    // icon.classList.add('far fa-trash-alt');
    // buttonX.appendChild(icon);

    
  
    li.appendChild(checkbox);
    li.appendChild(buttonX);
    
    ul.appendChild(li);
    document.querySelector('.listTasks').appendChild(ul);
    }
  }
