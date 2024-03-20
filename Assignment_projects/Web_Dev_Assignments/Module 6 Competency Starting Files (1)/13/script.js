/********w*************

	Do not alter this comment block. 
	Only fill out the information below.

	Competency 13 Event Listeners
	Name: 
	Date: 
	Description: 

**********************/

//	Task 1: Event listener to trigger the load function upon DOM loading
document.addEventListener("DOMContentLoaded", function(){
	load()
})

/*	
	Task 2
	Load function
	Event listeners to setup the page will go here
*/
function load() {
	const button = document.querySelector('button')
	button.addEventListener('click', function(){
		clickMe()
	})
}

/*
	Task 3
	Click Function
	This will change the display value of the input
*/
function clickMe() {
	const input = document.querySelector('input')
	if (input.style.display == 'block') {
		input.style.display = 'none'
	} else {
		input.style.display = 'block'
	}
}
