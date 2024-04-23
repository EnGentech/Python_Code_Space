/********w*************

    Do not alter this comment block. 
    Only fill out the information below.

    Competency 16
    Name: 
    Date:
    Description:

**********************/


/*
    Load function
    Using the fetch API, get your chosen dataset from the Dog API

 */
const load = () => {

    fetch("https://dog.ceo/api/breeds/list/all")
        .then(result => {
            return result.json();
        })
        .then(data => {
            createHTML(data);
        });

}

/*
    createHTML function
    Using your chosen Dog dataset, create at least 2 HTML elements 
    and add them to the provided HTML
*/
const createHTML = data => {
    const dogList = document.querySelector("#wrapper");
    const houseElement = document.createElement("div")
    const title = document.createElement("h1");
    title.textContent = "Dogs List";
    houseElement.appendChild(title);

    const listHead = document.createElement("ul");
    const listContent = document.createElement("li");

    for (const key in data.message) {
        const listContent = document.createElement("li");
        listContent.textContent = key;
        listHead.appendChild(listContent);
    }

    listHead.appendChild(listContent);
    houseElement.appendChild(listHead);
    dogList.appendChild(houseElement);

}

//adds an event listener to execute onLoad method when page finished loading
document.addEventListener("DOMContentLoaded", load);