//Demo 1
document.getElementById("demo").innerHTML=("Text Changed");

//Demo 5
function myFunction() {
    document.getElementById('demo2').innerHTML='Paragraph Changed';
}

//Demo 6
function innerFunction() {
    document.getElementById("demo3").innerHTML = "<h2>Hello World</h2>";
}

//Demo 7
function innerTextFunction() {
    document.getElementById("demo4").innerText = "Say hi to the world";
}

//Demo 8
function printFuction() {
    window.print();
}

//Demo 12
let a, b, c;
a = 5;
b = 6;
c = a + b;
document.getElementById("demo12").innerHTML = c;

//Demo 13
const cars = ["Volvo", "BMW", "Toyota"];

//Change the elemets
cars[0] = "Swift";

//Add a new elemets
cars.push("Audi");

//Display the Array
document.getElementById("demo13").innerHTML = cars ;
//Demo 13

//Demo 14
let text1 = "A";
let text2 = "B";
let result = text1 < text2;
document.getElementById("demo14").innerHTML= "A is grether than B " + result;

//Demo 15
// JavaScript Arrays
//Creating an Array
let fruits = ["Apple", "Banana", "Mango"];
console.log(fruits);

//You can access values by index (starting from 0):
console.log(fruits[0]);

//Array Length
console.log(fruits.length);

//Modifying Arrays
fruits[1] = 'Pineapple';
console.log(fruits);

//Adding/Removing Elements
fruits.push("grapes");// Add to end
console.log(fruits);

fruits.unshift("orange");// Add to start
console.log(fruits);

fruits.pop(); // Remove from end
console.log(fruits);

fruits.shift(); // Remove from start
console.log(fruits);

//Demo 16
//Looping Through Arrays
//For Loop
let numericNumbers = [1,2,3,4,5,6,7,8,9];
for (let i = 0; i < numericNumbers.length; i++) {
    console.log(numericNumbers[i]);
}

for (let i = 0; i < 5; i++) {
  console.log(i);
}

let nameValue = ['nandita', 'subrata', 'rakesh', 'rohit', 'krtitika'];
for (let n = 0; n < nameValue.length; n++) {
    console.log(nameValue[n]);
}

//while loop
//Runs while a condition is true.
//Useful when you don't know how many times you’ll loop.
let whileLoop = 0;
while (whileLoop < 7) {
  console.log(whileLoop);
  whileLoop++;
}

//do While Loop
//Similar to while, but runs at least once even if the condition is false.
let doWhile = 0;

do {
  console.log(doWhile);
  doWhile++;
} while (doWhile < 5);

//for...of loop
//Used to loop through arrays or iterables.
let fruitsName = ["apple", "banana", "cherry"];

for (let fruitDetais of fruitsName) {
  console.log(fruitDetais);
}

//for...in loop
//Used to loop through the keys (properties) of an object
let personDetais = { name: "Subrata", age: 25, job: "Dev" };

for (let key in personDetais) {
  console.log(key + ": " + personDetais[key]);
}

//Demo 17
//Function
function functionName() {
  // code to run
}

function sayHello() {
  console.log("Hello, Subrata!");
}
sayHello(); // calling the function

//Arrow Function
const add = (a, b) => a + b;
console.log(add(2, 5));

//Function with Return Value
function addValue(a , b) {
   return a + b ;
}
let valueResult = addValue(5 , 8);
console.log(valueResult);

//Destructring
const Dperson = { dName: "Alex", DAge: 30 };
const { dName, DAge } = Dperson;
console.log(dName);

//Spread Operator
const nums = [1, 2, 3];
const moreNums = [...nums, 4, 5];
console.log(moreNums); // [1, 2, 3, 4, 5]

//Using fetch()
fetch('https://jsonplaceholder.typicode.com/users')
  .then(res => res.json())
  .then(data => console.log(data));

//Demo 18
// Array of Objects
let arrayNames = [
    {name: "Subrata", age: 33, location: "kolkata"},
    {name: "Nandita", age: 25, location: "Burdwan"},
    {name: "Rajesh", age: 24, location: "Durgapur"},
]
console.log(arrayNames[1].age);//you can access the name/age/location indivitual as well
//Using forEach() loop to diplay the array
for (let i = 0; i < arrayNames.length; i++) {
  console.log(arrayNames[i].name + " is " + arrayNames[i].age + " years old");
}

//Demo 19
//map() – Create a new array by transforming each item
const authorData = [
    { title: "Atomic Habits", author: "James Clear" , age: 24 },
    { title: "The Alchemist", author: "Paulo Coelho" , age: 26 },
    { title: "Ikigai", author: "Francesc Miralles" , age: 30 }
]
const titles = authorData.map(function(writer) {
  return writer.author;
});
console.log(titles); 

//filter() – Create a new array with items that pass a condition
//Get users under age 26
const authorAge = authorData.filter(function(titles) {
  return titles.age < 26;
});
console.log(authorAge);

//find() – Get the first item that matches a condition
const findUser = authorData.find(function(authors) {
  return authors.author === "Francesc Miralles";
});
console.log(findUser);
// Output: { title: "Ikigai", author: "Francesc Miralles", age: 30 }


//Demo 16
const toggleBtn = document.getElementById("toggleBtn");
const title = document.getElementById("title");

toggleBtn.addEventListener("click", function (){
  const isDark = document.body.classList.contains("dark");

  //Ternary operator used here:
  document.body.className=isDark? "light" : "dark";
  title.textContent = isDark? "Light Mode" : "Dark Mode";
});






