/********w*************
    
	Project 3 Javascript
	Name:
	Date:
	Description:

**********************/

const itemDescription = ["MacBook", "The Razer", "WD My Passport", "Nexus 7", "DD-45 Drums"];
const itemPrice = [1899.99, 79.99, 179.99, 249.99, 119.99];
const itemImage = ["mac.png", "mouse.png", "wdehd.png", "nexus.png", "drums.png"];
let numberOfItemsInCart = 0;
let orderTotal = 0;

/*
 * Handles the submit event of the survey form
 *
 * param e  A reference to the event object
 * return   True if no validation errors; False if the form has
 *          validation errors
 */
function validate(e) {
	// Hides all error elements on the page
	hideErrors();

	// Determine if the form has errors
	if (formHasErrors()) {
		// Prevents the form from submitting
		e.preventDefault();
		displayValidationErrors();

		// When using onSubmit="validate()" in markup, returning false would prevent
		// the form from submitting
		return false;
	}

	// When using onSubmit="validate()" in markup, returning true would allow
	// the form to submit
	return true;


}

/*
 * Handles the reset event for the form.
 *
 * param e  A reference to the event object
 * return   True allows the reset to happen; False prevents
 *          the browser from resetting the form.
 */
function resetForm(e) {
	// Confirm that the user wants to reset the form.
	if (confirm('Clear order?')) {
		// Ensure all error fields are hidden
		hideErrors();

		// Set focus to the first text field on the page
		document.getElementById("qty1").focus();

		// When using onReset="resetForm()" in markup, returning true will allow
		// the form to reset
		return true;
	}

	// Prevents the form from resetting
	e.preventDefault();

	// When using onReset="resetForm()" in markup, returning false would prevent
	// the form from resetting
	return false;
}

function displayValidationErrors() {
    const fields = document.querySelectorAll('input[type="text"], input[type="number"]');

    fields.forEach(field => {
        const errorElement = document.getElementById(field.id + '_error');

        if (errorElement) {
            if (field.value.trim() === '') {
                errorElement.style.display = 'block';
            } else {
                errorElement.style.display = 'none';
            }
        }
    });
}


/*
 * Does all the error checking for the form.
 *
 * return   True if an error was found; False if no errors were found
 */
function formHasErrors() {
	// Determine if any items are in the cart
	// When the cart has not items, submission of form is halted
	if (numberOfItemsInCart == 0) {
		// Display an error message contained in a modal dialog element

		const modal = document.querySelector("#cartError");
		modal.showModal();

		const closeModal = document.querySelector(".close-button");

		closeModal.addEventListener("click", function() { // Anonymous function for click event
			modal.close();
			document.getElementById("qty1").focus();
		});

		// Form has errors
		return true;
	}

	//	Complete the validations below
	// Validate fullName input
	const fullName = document.getElementById("fullname").value;
	const address = document.getElementById("address").value;
	const city = document.getElementById("city").value;
	const email = document.getElementById("email").value;
	const postal = document.getElementById("postal").value
    const postalCodePattern = /^[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]\d$/;
	const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
	const cardSelect = document.getElementsByName("cardtype");
	const cartName = document.getElementById("cardname").value;
	const month = document.getElementById("month").value;
	const year = document.getElementById("year").value;
	const cardNumber = document.getElementById("cardnumber").value;

	let cardCheckStatus = 0
	const date = new Date();
	const currentYear = date.getFullYear();
	const currentMonth = date.getMonth() + 1;	

	for (let i = 0; i < cardSelect.length; i++) {
		if (cardSelect[i].checked) {
			cardCheckStatus = 1
			break
		}
	}

	let nonValidated = []

	if (cardNumber.length !== 10) {
		let cardError = document.getElementById("invalidcard_error");
		nonValidated.push(cardError)
    }

	const checkingFactors = [4, 3, 2, 7, 6, 5, 4, 3, 2];
	let sum = 0;
    for (let i = 0; i < checkingFactors.length; i++) {
        sum += checkingFactors[i] * parseInt(cardNumber.charAt(i));
    }
	const remainder = sum % 11;

	const digitCheck = 11 - remainder;
	const lastDigit = cardNumber.charAt(cardNumber.length - 1);

	if (digitCheck !== parseInt(lastDigit)) {
		let cardError2 = document.getElementById("invalidcard_error");
		nonValidated.push(cardError2)
	}

	if (!emailRegex.test(email)){
		let emailError = document.getElementById("emailformat_error");
		nonValidated.push(emailError)
	}

	if (!postalCodePattern.test(postal)){
		let postalError = document.getElementById("postalformat_error");
		nonValidated.push(postalError)
	}

	if (month.trim() === "- Month -"){
		let monthError = document.getElementById("month_error");
		nonValidated.push(monthError)
	}
	
	if ((year.trim() === "") || (year < currentYear) || ( year == currentYear && month < currentMonth)){
		let yearError = document.getElementById("expiry_error");
		nonValidated.push(yearError)
	}

	if (cardCheckStatus === 0){
		let checkStatusError = document.getElementById("cardtype_error");
		nonValidated.push(checkStatusError)
	}

	console.log(nonValidated)
	nonValidated.forEach(error => {
		error.style.display = "block";
	})

    if (
		(fullName.trim() === "") || (address.trim() === "") || 
		(city.trim() === "") || (!postalCodePattern.test(postal)) ||
		(!emailRegex.test(email) || (cardCheckStatus === 0) || (digitCheck !== parseInt(lastDigit)) ||
		(cartName.trim() === "") || (month.trim() === "- Month -") ||
		(year.trim() === "") || (year < currentYear) || ( year == currentYear && month < currentMonth))
	) {
        return true
    }
	

	// 	Complete the validations above

  return false; // Returning false by default if no errors found
}

/*
 * Adds an item to the cart and hides the quantity and add button for the product being ordered.
 *
 * param itemNumber The number used in the id of the quantity, item and remove button elements.
 */
function addItemToCart(itemNumber) {
	// Get the value of the quantity field for the add button that was clicked 
	let quantityValue = trim(document.getElementById("qty" + itemNumber).value);

	// Determine if the quantity value is valid
	if (!isNaN(quantityValue) && quantityValue != "" && quantityValue != null && quantityValue != 0 && !document.getElementById("cartItem" + itemNumber)) {
		// Hide the parent of the quantity field being evaluated
		document.getElementById("qty" + itemNumber).parentNode.style.visibility = "hidden";

		// Determine if there are no items in the cart
		if (numberOfItemsInCart == 0) {
			// Hide the no items in cart list item 
			document.getElementById("noItems").style.display = "none";
		}

		// Create the image for the cart item
		let cartItemImage = document.createElement("img");
		cartItemImage.src = "images/" + itemImage[itemNumber - 1];
		cartItemImage.alt = itemDescription[itemNumber - 1];

		// Create the span element containing the item description
		let cartItemDescription = document.createElement("span");
		cartItemDescription.innerHTML = itemDescription[itemNumber - 1];

		// Create the span element containing the quanitity to order
		let cartItemQuanity = document.createElement("span");
		cartItemQuanity.innerHTML = quantityValue;

		// Calculate the subtotal of the item ordered
		let itemTotal = quantityValue * itemPrice[itemNumber - 1];

		// Create the span element containing the subtotal of the item ordered
		let cartItemTotal = document.createElement("span");
		cartItemTotal.innerHTML = formatCurrency(itemTotal);

		// Create the remove button for the cart item
		let cartItemRemoveButton = document.createElement("button");
		cartItemRemoveButton.setAttribute("id", "removeItem" + itemNumber);
		cartItemRemoveButton.setAttribute("type", "button");
		cartItemRemoveButton.innerHTML = "Remove";
		cartItemRemoveButton.addEventListener("click",
			function () { // Anonymous function for click event
				// Removes the buttons grandparent (li) from the cart list
				this.parentNode.parentNode.removeChild(this.parentNode);

				// Deteremine the quantity field id for the item being removed from the cart by
				// getting the number at the end of the remove button's id
				let itemQuantityFieldId = "qty" + this.id.charAt(this.id.length - 1);

				// Get a reference to quanitity field of the item being removed form the cart
				let itemQuantityField = document.getElementById(itemQuantityFieldId);

				// Set the visibility of the quantity field's parent (div) to visible
				itemQuantityField.parentNode.style.visibility = "visible";

				// Initialize the quantity field value
				itemQuantityField.value = "";

				// Decrement the number of items in the cart
				numberOfItemsInCart--;

				// Decrement the order total
				orderTotal -= itemTotal;

				// Update the total purchase in the cart
				document.getElementById("cartTotal").innerHTML = formatCurrency(orderTotal);

				// Determine if there are no items in the car
				if (numberOfItemsInCart == 0) {
					// Show the no items in cart list item 
					document.getElementById("noItems").style.display = "block";
				}
			},
			false
		);

		// Create a div used to clear the floats
		let cartClearDiv = document.createElement("div");
		cartClearDiv.setAttribute("class", "clear");

		// Create the paragraph which contains the cart item summary elements
		let cartItemParagraph = document.createElement("p");
		cartItemParagraph.appendChild(cartItemImage);
		cartItemParagraph.appendChild(cartItemDescription);
		cartItemParagraph.appendChild(document.createElement("br"));
		cartItemParagraph.appendChild(document.createTextNode("Quantity: "));
		cartItemParagraph.appendChild(cartItemQuanity);
		cartItemParagraph.appendChild(document.createElement("br"));
		cartItemParagraph.appendChild(document.createTextNode("Total: "));
		cartItemParagraph.appendChild(cartItemTotal);

		// Create the cart list item and add the elements within it
		let cartItem = document.createElement("li");
		cartItem.setAttribute("id", "cartItem" + itemNumber);
		cartItem.appendChild(cartItemParagraph);
		cartItem.appendChild(cartItemRemoveButton);
		cartItem.appendChild(cartClearDiv);

		// Add the cart list item to the top of the list
		let cart = document.getElementById("cart");
		cart.insertBefore(cartItem, cart.childNodes[0]);

		// Increment the number of items in the cart
		numberOfItemsInCart++;

		// Increment the total purchase amount
		orderTotal += itemTotal;

		// Update the total puchase amount in the cart
		document.getElementById("cartTotal").innerHTML = formatCurrency(orderTotal);
	}
}

/*
 * Hides all of the error elements.
 */
function hideErrors() {
	// Get an array of error elements
	let error = document.getElementsByClassName("error");

	// Loop through each element in the error array
	for (let i = 0; i < error.length; i++) {
		// Hide the error element by setting its display style to "none"
		error[i].style.display = "none";
	}
}

/*
 * Handles the load event of the document.
 */

function load() {
	//	Populate the year select with up-to-date values
	let year = document.getElementById("year");
	let currentDate = new Date();
	hideErrors()
	for (let i = 0; i < 7; i++) {
		let newYearOption = document.createElement("option");
		newYearOption.value = currentDate.getFullYear() + i;
		newYearOption.innerHTML = currentDate.getFullYear() + i;
		year.appendChild(newYearOption);
	}

	// Add event listener for the form submit
	document.getElementById("orderform").addEventListener("submit", validate);

	// Add event listener for the form reset
	document.getElementById("orderform").addEventListener("reset", resetForm);

	// Add event listeners for the buttons to add items to the cart
	document.getElementById("addMac").addEventListener("click", function() { addItemToCart("1"); }); // Anonymous function for click event
	document.getElementById("addMouse").addEventListener("click", function() { addItemToCart("2"); }); // Anonymous function for click event
	document.getElementById("addWD").addEventListener("click", function() { addItemToCart("3"); }); // Anonymous function for click event
	document.getElementById("addNexus").addEventListener("click", function() { addItemToCart("4"); }); // Anonymous function for click event
	document.getElementById("addDrums").addEventListener("click", function() { addItemToCart("5"); }); // Anonymous function for click event
}

// Add document load event listener
document.addEventListener("DOMContentLoaded", load);
