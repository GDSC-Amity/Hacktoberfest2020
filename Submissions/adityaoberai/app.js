'use strict'

let today = new Date();
let formatDate = today.toDateString();
let selectElement = document.getElementById('date');
selectElement.innerHTML = formatDate;

console.log('Here\'s a hidden message');

// This is a single-line comment.

/* Here's a
multi-line
comment. */

// console.log('This code is no longer active')
