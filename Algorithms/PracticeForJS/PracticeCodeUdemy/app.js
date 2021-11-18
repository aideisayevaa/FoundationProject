/* let box=document.createElement('div')
box.className='circle'
box.style.width=`5px` */


/* console.log(this)

console.log(this.document)

console.log(document) */
/* 
let value;
value=document;
value=document.all;
value=document.all.length
value=document.all[0]

console.log(document.body)

value=document.location.hostname
value=document.location.port
value=document.URL
value=document.characterSet



console.log(value) */



/* let value;

value=document;
//scriptler
value=document.scripts;
console.log(value)

//-----------links-----------
value=document.links
value=document.links.length
value=document.links[0]
value=document.links[document.links.length-1]
value=document.links[document.links.length-1].className
value=document.links[document.links.length-1].classList
value=document.links[document.links.length-1].getAttribute("class")
value=document.links[document.links.length-1].getAttribute("href")


//-----------formlar-----------
value=document.forms
value=document.forms.length
value=document.forms[0]
value=document.forms["form"]
value=document.forms[0].id
value=document.forms[0].getAttribute("id")
value=document.forms[0].name
value=document.forms[0].getAttribute("name")

value=document.forms[0].method
console.log(value)
 */


/* const element=document.querySelector("#clear-todos") */


//--------------element xususiyyetleri------------------
/* console.log(element.id)
console.log(element.className)
console.log(element.classList);
console.log(element.classList[0]);
console.log(element.textContent); //sadece yazilari getirir
console.log(element.innerHTML);
console.log(element.href);

console.log(element.style);
 */

//---------style xususiyetleri deyisme---------------
/* element.className = "btn btn-danger" //bootstrap oldugu ucun bele oldu
element.style.color = "red"
element.style.marginLeft = "50px"
element.href = "https://www.google.com"
element.textContent = "silin" */
//-------------html tegi elave etme-----------------
/* element.innerHTML = "<span style = 'color: green'>Silin</span>"


const elements = document.querySelectorAll(".list-group-item");
elements.forEach(function(el){
    el.style.color = "red";
    el.style.background = "#000";
})
 */


/* let element2 = document.querySelector("li");//ilk li gelir
element2 = document.querySelector("li:first-child");//ilk li gelir
element2 = document.querySelector("li:last-child");//son li gelir
element2 = document.querySelector("li:nth-child(2)")//ikinci li gelir
element2 = document.querySelectorAll("li:nth-child(odd)")//tek yerde duran li-ler gelir
element2 = document.querySelectorAll("li:nth-child(event)")//cut yerde duran li-ler gelir

element2.forEach(function(el){
    el.style.background = "#ccc";

})
console.log(element2) */

// -------------------------108--------------------------
//Dom elementleri uzerinde gezinme
/* 
let value;

const todoList = document.querySelector(".list-group");
const todo = document.querySelector(".list-group-item:nth-child(2)");
const cardrow = document.querySelector(".card.row");

value = todoList;
value = todo;
value = cardrow;

//child nodes - text daxil 

value = todoList.childNodes;
value = todoList.childNodes[0];

//children - element

value = todoList.children;
value = todoList.children[0]; //ilk olani goturur
value = todoList.children[todoList.children.length - 1]; //son olani goturur
value = todoList.children[2].textContent = "Degisti";



value = cardrow;
value = cardrow.children;
value = cardrow.children[2].children[1].textContent = "Burasi da degisti";


value = todoList;
value = todoList.firstElementChild;
value = todoList.lastElementChild;
value = todoList.children.length;
value = todoList.childElementCount;


value = cardrow;
value = cardrow.parentElement;
value = cardrow.parentElement.parentElement;


value = todo;
value = todo.previousElementSibling;
value = todo.nextElementSibling;
value = todo.nextElementSibling.nextElementSibling;

value = todo.previousElementSibling.previousElementSibling
console.log(value)
 */

// -------------- 109 ------------------------
//  ------------- DInamik olaraq element yaratma -------------------
/* const newLink = document.createElement("a");
const cardbody = document.getElementsByClassName("cardbody[1]")

newLink.id = "clear-todos";
newLink.className = "brn btn-danger"
newLink.href = "https://www.google.com.tr"

//text content
cardbody.textContent = "kzjsdksj" //bu guvenli deyil butun hamsinin deyisir

/* //text node

const text = document.createTextNode("Salam")
cardbody.appendChild(text);
console.log(cardbody) */

/*newLink.appendChild(document.createTextNode("Farkli Sayfaya git"))

cardbody.appendChild(newLink)

console.log(newLink) */


// -------------- 110 ------------------------
//  ------------- DInamik olaraq element silme -------------------

/* const todoList = document.querySelector("ul.list-group");
const todos = document.querySelectorAll("li.list-group-item");

//Remove metodu

todos[1].remove();

//Remove Child

todoList.removeChild(todoList.lastElementChild);
todoList.removeChild(todos[3]);

console.log(todos);
console.log(todoList); */

// -------------- 112 ------------------------
//  ------------- Replace -------------------

/* const cardbody = document.querySelectorAll(".card-body")[1];

const newElement = document.createElement("h3")

newElement.className = "card-title";
newElement.id = "tasks-title";
newElement.textContent = "Yeni todolar";

//kohne element

const oldElement = document.querySelector("#tasks-title")

cardbody.replaceChild(newElement, oldElement);

console.log(newElement) */


const todoList = document.getElementById("todo");
let element;

element = todoInput;
element = todoInput.classList;

todoInput.classList.add("newClass");
todoInput.classList.add("newClas2");
todoInput.classList.remove("form-control");


element = todoInput;
element = todoInput.placeholder;
element = todoInput.getAttribute("placeholder");
todoInput.setAtttibute("placeholder","Salam");
todoInput.setAtttibute("title","Input");
todoInput.removeAttribute("name");

element = todoInput;
element = todoInput.hasAttribute("name");

console.log(element)
