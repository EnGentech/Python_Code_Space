/********w*************

    Do not alter this comment block. 
    Only fill out the information below.
    
    Competency 12 Javascript Syntax
    Name: 
    Date:
    Description:

**********************/

const favoriteQuotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
  ];
  
let quotesHTML = '';
for (let quote of favoriteQuotes) {
quotesHTML += `<p>${quote}</p>`;
}
  
const wrapper = document.createElement("div")
wrapper.innerHTML = quotesHTML

document.body.append(wrapper)
