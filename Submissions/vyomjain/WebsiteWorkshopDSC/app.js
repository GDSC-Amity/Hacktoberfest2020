'use strict';
console.log('js linked');
let today = new Date();
document.getElementById('date').innerHTML = today.toDateString();
document.getElementById("time").innerHTML = today.toLocaleTimeString();

var tasks = document.querySelectorAll(".list");
console.log(tasks);
tasks.forEach((items) => {
    items.addEventListener('click', ()=> {
        items.classList.add('done');
    })
})

console.log('Here\'s a hidden message: SHdWRE1Pakk3d2N0S2lBVU5LdUdaY25EYnBWZy9zbVJzVlZHZk9EeHZPMD06OveCND70jGjJleHam/vIUZY=');
// Try decoding that
/*choose a directory
number between
1 and 3*/