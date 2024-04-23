/********w*************

    Do not alter this comment block. 
    Only fill out the information below.

    Competency 17
    Name: 
    Date:
    Description:

**********************/

/*
    createZooland function
    This function will retrieve the data for the animal you created specifically
    You will then add the code required to meet the specifications
 */
    const createZooland = zoolandData => {
        const contentData = document.querySelector("#content");
    
        const myAnimal = zoolandData.find(animal => animal.common_name === "Fish");
    
        if (myAnimal) {
            const name = document.createElement("h2");
            const scientificName = document.createElement("h3");
            const description = document.createElement("blockquote");
            const imageContainer = document.createElement("div");
    
            name.textContent = myAnimal.common_name;
            scientificName.textContent = myAnimal.scientific_name;
            description.textContent = myAnimal.description;
    
            myAnimal.images.image.forEach(imageSrc => {
                const image = document.createElement("img");
                image.src = `images/${imageSrc}`;
                imageContainer.appendChild(image);
            });
    
            contentData.appendChild(name);
            contentData.appendChild(scientificName);
            contentData.appendChild(description);
            contentData.appendChild(imageContainer);
        } else {
            console.error("Your animal was not found in the JSON data.");
        }
    }
    

/*
    load function
        loading the json file - run when the page loads
 */
const load = () => {
    fetch('zooland.json')
        .then(result => {
            return result.json()
        })
        .then(data => {
            createZooland(data);
        });
}

//adds an event listener to execute onLoad method when page finished loading
document.addEventListener("DOMContentLoaded", load);
