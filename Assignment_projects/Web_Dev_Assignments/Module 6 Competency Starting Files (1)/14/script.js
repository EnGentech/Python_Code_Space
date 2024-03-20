/********w*************

    Do not alter this comment block. 
    Only fill out the information below.

    Competency 14 
    Name: 
    Date:
    Description:

**********************/

document.addEventListener("DOMContentLoaded", load);

const loremIpsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

/*	
    Load function
    Create, insert, and delete elements
*/
function load() {
    const pElement = document.createElement('p')
    pElement.textContent = `${loremIpsum}`
    const resultElement = document.getElementById('results')
    resultElement.appendChild(pElement)

    const h2Element = document.createElement('h2')
    h2Element.textContent = 'Lorem Ipsum'
    resultElement.insertBefore(h2Element, pElement)

    const deleteFooter = document.querySelector('footer')
    deleteFooter.remove()
}




