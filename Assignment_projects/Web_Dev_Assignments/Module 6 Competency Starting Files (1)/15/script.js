/********w*************

	Do not alter this comment block. 
	Only fill out the information below.
	
	Competency 15
	Name: 
	Date:
	Description:

*********************/

document.addEventListener("DOMContentLoaded", load);

function load() {
	let calcButton = document.getElementById('calcButton');

	calcButton.addEventListener('click', calc);
	clearFields();

}

function calc() {
	let name = document.getElementById('fullName').value;
	let hours = document.getElementById('hoursWorked').value;
	let rate = document.getElementById('hourlyRate').value;

	if (name == "" || hours == "" || rate == "") {
		clearFields();
		return;
	}

	let pay = calcPay(hours, rate);
	let taxes = getTax(pay);
	let net = pay - taxes;

	printRow(name, pay.toFixed(2), taxes.toFixed(2), net.toFixed(2));
	clearFields();
}

function clearFields() {
	document.getElementById('fullName').value = "";
	document.getElementById('hoursWorked').value = "";
	document.getElementById('hourlyRate').value = "";
	document.getElementById('fullName').focus();

}


/*
	calcPay function
	receives hours and hourly rate values
	returns the calculated pay
*/
function calcPay(hours, rate) {
	let totalPay = 0;
	if (Number(hours) <= 40) {
		totalPay = Number(hours) * Number(rate)
	} else {
		let overtime = Number(hours) - 40;
		totalPay = (40 * Number(rate)) + (overtime * (Number(rate) * 1.5));
	}
	return totalPay
}

/*
	getTax function
	receives gross pay
	returns relative tax rate
*/
function getTax(funcGross) {
	let funcTax = 0;
	if (funcGross < 250) {
		funcTax = funcGross * .25;
	}
	else {
		if (funcGross < 500) {
			funcTax = funcGross * .3;
		}
		else {
			if (funcGross <= 750) {
				funcTax = funcGross * .4;
			}
			else {
				funcTax = funcGross * .5;
			}
		}
	}
	return funcTax;
}

/* 
	printRow function
	receives name, gross, taxes, and net pay
	formats currency
	prints a row in the table
*/
function printRow(name, gross, taxes, net) {
	//	Set values to 2 decimal places here


	let tbody = document.getElementsByTagName("tbody")[0];
	let tr = document.createElement("tr");
	let td = document.createElement("td");
	let td1 = document.createElement("td");
	let td2 = document.createElement("td");
	let td3 = document.createElement("td");

	td.innerHTML = name;
	td1.innerHTML = `$${gross}`;
	td2.innerHTML = `$${taxes}`;
	td3.innerHTML = `$${net}`;

	tr.appendChild(td);
	tr.appendChild(td1);
	tr.appendChild(td2);
	tr.appendChild(td3);

	tbody.appendChild(tr);
}

