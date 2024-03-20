let circle = document.getElementById("circle")
document.getElementById("submit").onclick = function(){
    let shape = document.getElementById("color").value
    circle.style.backgroundColor = shape
    if(shape === "square"){
        circle.style.borderRadius = "0%"
        circle.style.width = "120px"
        circle.style.height = "120px"
    } else if (shape === "circle"){
        circle.style.width = "120px"
        circle.style.height = "120px"
        circle.style.borderRadius = "50%"
    } else if (shape === "rectangle"){
        circle.style.width = "120px"
        circle.style.height = "60px"
        circle.style.borderRadius = "0%"
    }
    
}

// document.getElementById("dark_mode").onclick = function(){
//     let changeMode = document.getElementById("changeMode")
//     circle.style.backgroundColor = "white"
//     changeMode.style.backgroundColor = "black"
// }

// document.getElementById("white_mode").onclick = function(){
//     let changeMode = document.getElementById("changeMode")
//     circle.style.backgroundColor = "black"
//     changeMode.style.backgroundColor = "white"
// }

